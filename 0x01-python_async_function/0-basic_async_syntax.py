#!/usr/bin/env python3
"""
An asynchronous coroutine that takes in an integer argument that waits for a delay
"""


import asyncio
import random
import sys


async def wait_random(max_delay = 10):
    max_delay = sys.argv[1]
    random_delay = random.randint(max_delay)
    return await asyncio.sleep(random_delay)
