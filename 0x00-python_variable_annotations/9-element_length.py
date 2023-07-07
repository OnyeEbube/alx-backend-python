#!/usr/bin/bash
"""Annotates a function's parameters and return values"""


from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a List of Tuples"""
    return [(i, len(i)) for i in lst]
