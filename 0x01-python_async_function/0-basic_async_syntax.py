#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument that waits for a delay
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Wait for some time """
    random_delay = random.random() * max_delay
    await asyncio.sleep(random_delay)
    return random_delay
