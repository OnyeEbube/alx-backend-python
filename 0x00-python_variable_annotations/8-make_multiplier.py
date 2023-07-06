#!/usr/bin/env python3
from typing import Callable
"""A type-annotated function make_multiplier"""


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
