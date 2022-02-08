# Survey of Python's Async Features

This is a survey of python's async concurrency features by example.

The purpose of this survey is to demonstrate that using Python's async features isn't difficult, and
they are simple to use in all IO bound contexts. They can be used
simply and to great effect in scripts, existing sync backends, ETLs, wherever.

Most examples necessarily demonstrate how to interop with synchronous code, because all python
programs begin in a blocking main thread. The event loop must be explicitly evoked and given control
of the main thread. The interop examples become more useful in later parts. 

Sync/Async interop is particularly necessary in a language that introduced async features after the fact. 
Python supplies several ways for async code to easily await on blocking functions (from, for instance, db drivers 
that block on io) without halting the event loop. Some of these techniques are covered in later sections.

## When to use these features?

Whenever the program's performance is constrained by the performance of the hosts I/O subsystem. 
In other words, I/O bound contexts. This is usually contrasted with CPU bound applications, where
the applications performance is dependent on the speed of the CPU. If the CPU in question has multple cores,
the event loop, having a single execution thread, cannot execute multiple coroutines in parallel.

However, Python's async features could still be useful in dispatching and coordinating work between 
coroutines and different process workers, which can take advantage of multi core CPU's. Python provides some
useful abstractions (e.g. Executors) which are designed to interop between the event loop and 
python threads/processes.

## Why not use python multithreading for an IO Bound application?

_NOTE: Generally, the GIL ensures that only one thread can execute at once._

1. There is effectively an event loop anyway, but the operating system decides which thread should execute and for how long.
2. The operating system doesn't understand how the threads should cooperate. Therefore opens the possiblity of race conditions and unsafe operations on memory unless the program
   accounts for the unpredictable nature of threaded execution (via locks, queues, etc.). In otherwords, the program has to be written to cooperate after the fact, versus
   an environment which is inherently cooperative.
3. Threads have overhead.

Versus async concurrency:

1. The programmer controls context switching between execution units.
2. The event loop executes in a single thread, and the coroutines must explicitly yield back control making race conditions impossible. Also, since
   only one coroutine can execute at once, memory access and mutation is incidentally atomic.
3. One call stack, versus one per thread (in additon to other overhead from OS thread). Also, exceptions are easier to trace, because there is one
   stack.

## Setup

```bash
make build
make server
# new tab or terminal window
make part_<01-16>
```

## Index

### Event Loop

1.  [Obtaining or creating the event loop](./part_01.py)

2.  [Scheduling and running a coroutine to completion on the event loop](./part_02.py)


### Awaitables
  
3.  [Coroutines](./part_03.py)

4.  [Futures](./part_04.py)

5.  [Tasks](./part_05.py)

6.  [Awaitable Objects](./part_06.py)

7.  [Async Context Managers](./part_07.py)

8.  [Async Iterators](./part_08.py)

9.  [Async Generators](./part_09.py)


### Concurrency

10. [Via loop.create_task](./part_10.py)

11. [Via asyncio.gather (asyncio.sleep example)](./part_11.py)

12. [Via asyncio.gather (aiohttp example)](./part_12.py)

13. [Via asyncio.as_completed](./part_13.py)


### Sync / Async Interop

14. [loop.run_in_executor (thread pool, io bound)](./part_14.py)

15. [loop.run_in_executor (process pool, cpu bound)](./part_15.py)


### Extras

16. [async queue consumer / producer](./part_16.py)

17. [asyncio Stream API - mini redis](./part_17.py)