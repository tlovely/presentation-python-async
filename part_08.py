"""
Implicit Awaitables - Async Iterator
"""
import asyncio

print(__doc__)

loop = asyncio.get_event_loop()


async def main():
    async def sleep(s):
        print(f"sleep {s} start")
        await asyncio.sleep(s)
        print(f"sleep {s} end")

    class ai:
        def __init__(self, a, b):
            self._a = a - 1
            self._b = b

        def __aiter__(self):
            print("aiter")
            return self

        async def __anext__(self):  # exception type, value, and traceback
            if self._a == self._b:
                raise StopAsyncIteration()
            self._a += 1
            await sleep(0.1)
            return self._a


    async for i in ai(0, 10):
        print(i)


if __name__ == "__main__":
    loop.run_until_complete(main())