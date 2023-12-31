#!/usr/bin/env python3
"""A type-annotated function sum_list"""

from typing import List


def sum_list(input_list:  List[float]) -> float:
    """returns their sum as a float"""
    sums = 0
    for i in input_list:
        sums += i
    return float(sums)
