#!/usr/bin/env python3
""" Contains a type-annotated function safely_get_value """
from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """ Return the value of a given key or None """
    if key in dct:
        return dct[key]
    else:
        return default
