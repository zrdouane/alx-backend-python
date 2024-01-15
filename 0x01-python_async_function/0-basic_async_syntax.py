#!/usr/bin/env python3
"""
module asynchronous tasks using asyncio.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait a random amount of time up to `max_delay` seconds.
    Returns the amount of time waited.
    """
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
