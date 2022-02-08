"""
Implicit Awaitables - Async Generators (PEP 525)
"""
import asyncio

loop = asyncio.get_event_loop()


async def main():
    async def sleep(s):
        print(f"sleep {s} start")
        await asyncio.sleep(s)
        print(f"sleep {s} end")

    
    async def ag(a, b):
        for i in range(a, b + 1):
            await sleep(0.1)
            yield i


    async for i in ag(0, 10):
        print(i)


    async def sleep_return(s, v):
        await sleep(s)
        return v


    # async genrator comprehension
    agc = (i * 10 async for i in ag(0, 10))

    async for i in agc:
        print(i)


if __name__ == "__main__":
    loop.run_until_complete(main())