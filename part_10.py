"""
Concurrency - Async - Tasks
"""
import asyncio

print(__doc__)

loop = asyncio.get_event_loop()


async def printer(s, delay, stop_tick=-1):
    t = stop_tick
    while t != 0:
        print(s)
        await asyncio.sleep(delay)
        t -= 1
    print(f"{s} end")


if __name__ == "__main__":
    # create_task creates asyncio.Task and schedules it on the event loop
    loop.create_task(printer("Task 1", 1, -1))
    loop.create_task(printer("Task 2", 2, -1))
    loop.create_task(printer("Task 3", 3, 3))
    
    loop.run_forever()