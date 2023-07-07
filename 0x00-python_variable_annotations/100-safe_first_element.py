#!/usr/bin/env python3
"""Augumenting the code with correct duck-typed annotations"""


from typing import Union, Sequence, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
