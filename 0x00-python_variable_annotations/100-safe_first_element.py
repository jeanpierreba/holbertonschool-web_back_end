#!/usr/bin/env python3
""" Contains a type-annotated function safe_frist_element """
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ Return element of a list or None """
    if lst:
        return lst[0]
    else:
        return None
