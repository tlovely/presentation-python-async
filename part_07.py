"""
Implicit Awaitables - Async Context Managers
"""
import asyncio

loop = asyncio.get_event_loop()


async def main():
    async def sleep(s):
        print(f"sleep {s} start")
        await asyncio.sleep(s)
        print(f"sleep {s} end")

    class cm:
        async def __aenter__(self):
            print("aenter start")
            await sleep(0.5)
            print("aenter end")
            return self

        async def __aexit__(self, t, v, b):  # exception type, value, and traceback
            print("aexit start")
            await sleep(1)
            print("aexit end")


    async with cm() as a:
        pass


if __name__ == "__main__":
    loop.run_until_complete(main())