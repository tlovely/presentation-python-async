"""
Awaitables - Futures
"""
import asyncio

loop = asyncio.get_event_loop()


async def main():
    print("-- futures --")
    f = asyncio.Future()
    assert f.done() == False
    f.set_result("Future resolved")  # unless we do this, awaiting on f will hang indefinately
    assert f.done() == True
    # await here polls future on whether it is done or cancelled, then returns Future.result().
    # if an exception was passed to Future.set_exception(<exception instance>), done() will be true, and calling
    # result will throw that exception.
    print(await f)
    # futures can be awaited multiple times for the same result
    print(await f)


if __name__ == "__main__":
    loop.run_until_complete(main())