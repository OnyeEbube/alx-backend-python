#!/usr/bin/env python3
"""A type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
