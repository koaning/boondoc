from typing import List


def some_func(inputs:List[str], foo: str) -> None:
    """
    Some function that does things.
    """
    for item in inputs:
        print(item, foo)

class Foobar:
    def __init__(self, stuff):
        self.stuff = stuff 
    
    def printstuff(self):
        print(stuff)
