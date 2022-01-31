#!/usr/bin/env python3
""" Contains a type-annotated function element_length """
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Take lst as an argument and return a list of tuples """
    return [(i, len(i)) for i in lst]
