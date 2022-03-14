#!/usr/bin/env python3

import redis
from uuid import uuid4
from typing import Callable, Union, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count number of calls """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ wrapper function that increments """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ store the history of inputs and outputs """
    input = method.__qualname__ + ":inputs"
    output = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """ Wrapper that store lists """
        self._redis.rpush(input, str(args))
        return_method = method(self, *args, **kwds)
        return self._redis.rpush(output, str(return_method))
    return wrapper


def replay(method: Callable):
    """ display the history of calls """
    r = redis.Redis()
    name = method.__qualname__
    counter = r.get(name).decode("utf-8")
    input = r.lrange(name + ":inputs", 0, -1)
    output = r.lrange(name + ":outputs", 0, -1)
    print("{} was called {} times:".format(name, counter))
    for i, j in zip(input, output):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     j.decode('utf-8')))


class Cache:
    """ Cache class for redis """

    def __init__(self):
        """ Initialize redis model """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ generate a random key store the input data in Redis
        using the random key and return the key """
        key = str(uuid4())
        self._redis.mset({key: data})
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
            str, bytes, int, float]:
        """ onvert the data back to the desired format """
        if fn:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, string: bytes) -> str:
        """ get a string """
        return string.decode("utf-8")

    def get_int(self, data: str) -> int:
        """ Converts the data to int """
        return int(self._redis.get(data))
