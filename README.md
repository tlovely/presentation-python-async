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