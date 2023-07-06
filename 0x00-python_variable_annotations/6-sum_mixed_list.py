#!/usr/bin/env python3
"""A type-annotated function sum_mixed_list"""


from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """returns their sum as a float"""
    sums = 0.0
    for i in mxd_list:
        sums += i
    return sums

