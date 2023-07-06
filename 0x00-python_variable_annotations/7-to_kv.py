#!/bin/usr/env python3
from typing import Union
from typing import Tuple
"""A type-annotated function to_kv"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    if isinstance(v, int):
        v = float(v)
    return (k, v**2)
