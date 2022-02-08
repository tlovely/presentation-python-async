"""
Concurrency - Async - asyncio.gather (with aiohttp)
"""
import asyncio
import requests

from aiohttp import ClientSession

loop = asyncio.get_event_loop()
run = loop.run_until_complete


async def a_http_get(session, delay):
    print(f"Task {delay} start")
    response = await session.get(f"http://localhost:8000/count?delay={delay}")
    v = await response.json()
    print(f"Task {delay} end")
    return v


async def http_get(delay):
    print(f"Task {delay} start")
    response = requests.get(f"http://localhost:8000/count?delay={delay}")
    print(f"Task {delay} end")
    return response.json()


if __name__ == "__main__":
    # create_task creates asyncio.Task and schedules it on the event loop
    session = ClientSession()
    values = run(asyncio.gather(*(
        a_http_get(session, i) for i in range(5)
    )))
    run(session.close())
    print(values)
    # this blocks the event loop, and nothing runs concurrently
    values = loop.run_until_complete(asyncio.gather(*(
        http_get(i) for i in range(5)
    )))
    print(values)