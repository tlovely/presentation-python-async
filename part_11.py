"""
Concurrency - Async - asyncio.gather (with asyncio.sleep)
"""
import asyncio
import time

print(__doc__)

loop = asyncio.get_event_loop()


async def a_sleep_return(s):
    print(f"Task {s} start")
    await asyncio.sleep(s)
    print(f"Task {s} end")
    return s


async def sleep_return(s):
    print(f"Task {s} start")
    time.sleep(s)
    print(f"Task {s} end")
    return s


if __name__ == "__main__":
    # create_task creates asyncio.Task and schedules it on the event loop
    values = loop.run_until_complete(asyncio.gather(*(
        a_sleep_return(i) for i in range(5)
    )))
    print(values)
    # this blocks the event loop, and nothing runs concurrently
    values = loop.run_until_complete(asyncio.gather(*(
        sleep_return(i) for i in range(5)
    )))
    print(values)