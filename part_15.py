"""
Sync / Async - loop.run_in_executor (process pool, cpu bound)
"""
import asyncio
import requests

from concurrent.futures import ProcessPoolExecutor


loop = asyncio.get_event_loop()
run = loop.run_until_complete

def compute_range_sum(a, b):
    return sum(range(a, b + 1))


if __name__ == "__main__":
    pool = ProcessPoolExecutor()  # max workers is by default number of cpus
    tasks = [
        loop.run_in_executor(
            pool, 
            compute_range_sum,
            1, 30_000_000 * m
        )
        for m in range(16)
    ]
    for task in asyncio.as_completed(tasks):
        print(run(task))