"""
Accessing the event loop
"""
import asyncio

# gets default event loop
loop = asyncio.get_event_loop()

# get_event_loop always returns the default
assert loop == asyncio.get_event_loop()

# to create a new event loop
loop_2 = asyncio.new_event_loop()
assert loop != loop_2

# a new default can also be set
asyncio.set_event_loop(loop_2)
# the default no longer equals the original
assert loop != asyncio.get_event_loop()