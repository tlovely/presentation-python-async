"""
Concurrency - Async - asyncio.as_completed
"""
import asyncio

from aiohttp import ClientSession

print(__doc__)

loop = asyncio.get_event_loop()
run = loop.run_until_complete


async def a_http_get(session, delay):
    print(f"Task {delay} start")
    response = await session.get(f"http://localhost:8000/count?delay={delay}")
    v = await response.json()
    print(f"Task {delay} end")
    return v


if __name__ == "__main__":
    # create_task creates asyncio.Task and schedules it on the event loop
    session = ClientSession()
    tasks = [a_http_get(session, i) for i in range(5)]
    for task in asyncio.as_completed(tasks):
        print(run(task))
    run(session.close())
