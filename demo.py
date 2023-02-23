from file import some_func, Foobar
from pprint import pprint
import inspect
import textwrap
import typing 
import jinja2
from lazylines import LazyLines


def parse_properties(thing):
    type_hints = typing.get_type_hints(thing)
    return {
        "name": thing.__name__, 
        "type": type(thing).__name__,
        "qualname": thing.__qualname__,
        "inputs": {k: v.__name__ for k, v in type_hints.items() if k != "return"},
        "output": type_hints["return"].__name__ if "return" in type_hints else "",
        "doc": textwrap.dedent(thing.__doc__).strip() if thing.__doc__ else "",
        "module": inspect.getmodule(thing).__name__
    }

def render_properties(properties):
    template = jinja2.Template("""##{{name}}""")
    return template.render(**properties)

props = parse_properties(LazyLines.mutate)
pprint(props)

print(render_properties(props))
