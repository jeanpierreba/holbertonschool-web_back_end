#!/usr/bin/env python3
""" contains an asynchronous coroutine """
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ takes an integer max_delay and returns a asyncio.Task """
    delays_list = []
    for i in range(n):
        delays_list.append(await task_wait_random(max_delay))
    return sorted(delays_list)
