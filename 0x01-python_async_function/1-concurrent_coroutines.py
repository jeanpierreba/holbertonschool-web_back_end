#!/usr/bin/env python3
""" contains an asynchronous coroutine """
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Return the list of all the delays """
    delays_list = []
    for i in range(n):
        delays_list.append(await wait_random(max_delay))
    return sorted(delays_list)
