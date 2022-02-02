#!/usr/bin/env python3
""" contains an asynchronous coroutine """
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_item(n: int, max_delay: int) -> float:
    """ returns total_time / n """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return (time.perf_counter() - start) / n
