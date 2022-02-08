"""
Sync / Async - loop.run_in_executor (thread pool, io bound)
"""
import asyncio
import requests

loop = asyncio.get_event_loop()
run = loop.run_until_complete


if __name__ == "__main__":
    # create_task creates asyncio.Task and schedules it on the event loop
    tasks = [
        loop.run_in_executor(
            None, 
            requests.get, 
            f"http://localhost:8000/count?delay={delay}"
        )
        for delay in range(5)
    ]
    for task in asyncio.as_completed(tasks):
        response = run(task)
        print(response.json())