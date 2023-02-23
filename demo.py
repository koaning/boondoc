from typing import List


def some_func(inputs:List[str], foo: str) -> None:
    """
    Some function that does things.
    """
    for item in inputs:
        print(item, foo)


import inspect
import textwrap
import typing 

print(typing.get_type_hints(some_func))
print(textwrap.dedent(some_func.__doc__))


def parse_properties(thing):
    type_hints = typing.get_type_hints(some_func)
    return {
        "name": thing.__name__, 
        "inputs": {k: v.__name__ for k, v in type_hints.items() if k != "return"},
        "output": type_hints["return"].__name__,
        "doc": thing.__doc__.strip()
    }

print(parse_properties(some_func))
