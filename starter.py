from dataclasses import dataclass
from collections.abc import Sequence

@dataclass
class Point:
    latitude: float
    longitude: float


class Items(Sequence):
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
        return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)







p = Point
print(p.__annotations__)
