#!/usr/bin/env python3
from typing import Union
from typing import Tuple
"""A type-annotated function to_kv"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """returns a tuple consisting of k and v as float"""
    return (k, float(v * v))
