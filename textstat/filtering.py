from __future__ import annotations

import operator
from dataclasses import dataclass
from typing import Callable, Type


@dataclass
class Comparison:
    objtype: Type
    property_name: str
    operation: Callable[[object, object], bool]
    other: object

    @property
    def type_name(self):
        return f"{self.objtype.__name__.lower()}s"

    def compare(self, item):
        return self.operation(getattr(item, self.property_name), self.other)


class filterable:
    def __init__(self, prop: property):
        self.prop: property = prop

    def __get__(self, obj, objtype=None):
        if obj is None:

            class Comparable:
                """An object that can be 'compared' to"""

                def __init__(self, prop):
                    self.prop_name = prop.fget.__name__

                def __lt__(self, other):
                    return Comparison(objtype, self.prop_name, operator.lt, other)

                def __gt__(self, other):
                    return Comparison(objtype, self.prop_name, operator.gt, other)

                def __le__(self, other):
                    return Comparison(objtype, self.prop_name, operator.le, other)

                def __ge__(self, other):
                    return Comparison(objtype, self.prop_name, operator.ge, other)

                def contains(self, other):
                    return Comparison(objtype, self.prop_name, operator.contains, other)

                def startswith(self, other):
                    return Comparison(objtype, self.prop_name, str.startswith, other)

                def endswith(self, other):
                    return Comparison(objtype, self.prop_name, str.endswith, other)

            return Comparable(self.prop)

        return self.prop.fget(obj)

    def __set__(self, obj, value):
        if not self.prop.fset:
            raise AttributeError(f"can't set attribute '{self.prop.fget.__name__}'")

        return self.prop.fset(obj, value)
