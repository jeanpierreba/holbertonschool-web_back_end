#!/usr/bin/env python3
""" contains a function named index_range """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ return a tuple of size two containing
    a start index and an end index """
    return ((page - 1) * page_size, page_size * page)
