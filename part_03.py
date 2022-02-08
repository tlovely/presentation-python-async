"""
Awaitables - Coroutines
"""
import asyncio

print(__doc__)

loop = asyncio.get_event_loop()


async def main():
    async def fn():
        print("Start")
        await asyncio.sleep(1)
        print("End")

    c = fn()
    await c
    # awaiting on this a second time will result in a RuntimeError because it has
    # already been "consumed" similar to a generator
    # try:
    await c
    # except RuntimeError as e:
    #     pass


if __name__ == "__main__":
    loop.run_until_complete(main())