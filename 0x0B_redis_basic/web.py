#!/usr/bin/env python3
""" obtain the HTML content of a particular URL """

import redis
import requests

redi = redis.Redis()
counter = 0


def get_page(url: str) -> str:
    """ ses the requests module to obtain the
    HTML content of a particular URL and returns it """
    data = f"count:{url}"
    redi.set(data, counter)
    request_url = requests.get(url)
    redi.incr(data)
    redi.setex(data, 10, redi.get(data))
    return request_url.text


if __name__ == "__main__":
    get_page('http://slowwly.robertomurray.co.uk')
