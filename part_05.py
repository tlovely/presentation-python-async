"""
Awaitables - Tasks
"""
import asyncio

print(__doc__)

loop = asyncio.get_event_loop()


async def main():
    # Takes a coroutine, not just any awaitable. When scheduled, the task
    # will await on the coroutine and will call set_result on itself, or
    # set_exception if an exception occurs
    t = asyncio.Task(asyncio.sleep(1))
    print("Start task")
    await t
    print("End task")
    # Since Tasks are a subclass of Futures, they include the same api.
    # for example, they can be awaited on multiple times
    await t
    assert t.done() == True


if __name__ == "__main__":
    loop.run_until_complete(main())