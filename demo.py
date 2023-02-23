from file import some_func, Foobar
from pprint import pprint
import inspect
import textwrap
import typing 
import jinja2
from lazylines import LazyLines


def parse_properties(thing):
    type_hints = typing.get_type_hints(thing)
    mod = inspect.getmodule(thing)

    return {
        "name": thing.__name__, 
        "type": type(thing).__name__,
        "qualname": thing.__qualname__,
        "inputs": {k: v.__name__ for k, v in type_hints.items() if k != "return"},
        "output": type_hints["return"].__name__ if "return" in type_hints else "",
        "doc": textwrap.dedent(thing.__doc__).strip() if thing.__doc__ else "",
        "module": mod.__name__ if mod else None     
    }


def render_properties(properties):
    template_string = """
    ## {{qualname}}({{inputs}})

    {{doc}}
    """
    template = jinja2.Template(textwrap.dedent(template_string))
    return template.render(**properties)


def get_codeblock_members(*classes):
    """
    Grabs the docstrings of any methods of any classes that are passed in.
    """
    results = []
    for cl in classes:
        if cl.__doc__:
            results.append(cl)
        for name, member in inspect.getmembers(cl, predicate=inspect.isfunction):
            if member.__doc__:
                results.append(member)
    return results

for m in get_codeblock_members(LazyLines):
    # print(m)
    props = parse_properties(m)
    # pprint(props)
    print(render_properties(props))
