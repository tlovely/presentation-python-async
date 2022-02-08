"""
Coroutine & Evoking the Event Loop (basic)

Generally, a coroutine is a control structure that 
encapsulates a unit of work which is designed to co-op with other coroutines by periodically ceding 
control back to the event loop.

An event loop is the he thing which executes on and decides which coroutine to supply the execution 
thread to next, once the active coroutine yields control.

A coroutine in python is the most basic awaitable.

It is essentially a generator in python where, internally, yield cedes control back to
the event loop, and StopIteration signals to the loop that the coroutine has
successfully resolved. Whatever is returned in the generator is attached to the exception, extracted, 
and returned in an await expression.
"""
import asyncio

print(__doc__)

loop = asyncio.get_event_loop()


async def fn():
    print("Start")
    await asyncio.sleep(1)
    print("End")


if __name__ == "__main__":
    # run_until_complete received an awaitable, wraps it in an asyncio.Task
    # with a done callback which will stop the event loop
    # (another type of awaitable, based on asyncio.Future), and ticks the 
    # event loop.
    loop.run_until_complete(fn())