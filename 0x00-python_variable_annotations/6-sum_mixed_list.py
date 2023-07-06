#!/usr/bin/env python3
from typing import Union
"""A type-annotated function sum_mixed_list"""


def sum_mixed_list(mxd_list: Union[int, float]) -> float:
    sums = 0
    for i in mxd_list:
        sums += i
    return float(sums)

