"""
Awaitables - Custom
"""
import asyncio

print(__doc__)

loop = asyncio.get_event_loop()


async def main():
    class a:
        def __await__(self):
            yield  # at least one yield is required, otherwise __await__ won't return a generator
            return 1  # is passed to StopIteration(<here>), and is available on the instance at e.value

    print(await a())

    def print_return(v):
        print(v)
        return v

    # interfacing with awaitables in __await__
    class b:
        def __await__(self):
            yield from asyncio.sleep(1).__await__()
            # with the statement "yield from", the left hand value will be whatever was returned by the generator being consumed
            # -------
            # since "yield from" is a statement, and the return statement requires an expression, we can't do this:
            # "return yield from" <-- syntax error 
            v = yield from a().__await__()
            return v 

    b = b()

    print(await b)
    # these can be awaited on more than once, and, unlike futures, will execute each time
    print(await b)


if __name__ == "__main__":
    loop.run_until_complete(main())