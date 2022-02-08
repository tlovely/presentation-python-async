"""
Queue Consumer / Producer
"""
import asyncio

print(__doc__)

async def consumer(n, queue):
    while True:
        v = await queue.get()
        print(f"{n}: {v}")


async def producer(queue):
    i = 0
    while True:
        await queue.put(i)
        await asyncio.sleep(0.1)
        i += 1


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    q = asyncio.Queue()
    loop.run_until_complete(q.put(1))
    loop.run_until_complete(asyncio.gather(
      consumer("a", q),
      consumer("b", q),
      consumer("c", q),
      producer(q),
    ))





