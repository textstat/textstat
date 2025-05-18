from __future__ import annotations

from typing import TYPE_CHECKING, Callable, Type

if TYPE_CHECKING:  # pragma: no cover
    from textstat.core.mixins.stats import Stats


import operator
from dataclasses import dataclass


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


def make_comparable(name: str, objtype):
    class Comparable:
        """An object that can be 'compared' to"""

        def __init__(self, prop_name: str):
            self.prop_name = prop_name

        def __eq__(self, other: object) -> Comparison:
            return Comparison(objtype, self.prop_name, operator.eq, other)

        def __lt__(self, other: object) -> Comparison:
            return Comparison(objtype, self.prop_name, operator.lt, other)

        def __gt__(self, other: object) -> Comparison:
            return Comparison(objtype, self.prop_name, operator.gt, other)

        def __le__(self, other: object) -> Comparison:
            return Comparison(objtype, self.prop_name, operator.le, other)

        def __ge__(self, other: object) -> Comparison:
            return Comparison(objtype, self.prop_name, operator.ge, other)

        def contains(self, other: object) -> Comparison:
            return Comparison(objtype, self.prop_name, operator.contains, other)

        def startswith(self, other: object) -> Comparison:
            return Comparison(objtype, self.prop_name, str.startswith, other)

        def endswith(self, other: object) -> Comparison:
            return Comparison(objtype, self.prop_name, str.endswith, other)

    return Comparable(name)


class _textstatproperty:
    def __init__(self, fget: Callable) -> None:
        self.fget = fget
        self.owner_class: Type["Stats"] | None = None

    def __set__(self, obj, value):
        raise AttributeError(f"can't set attribute '{self.fget.__name__}'")

    def __set_name__(self, owner: Type["Stats"], _: str) -> None:
        self.owner_class = owner


class textproperty(_textstatproperty):
    def __init__(self, fget: Callable) -> None:
        super().__init__(fget)

    def __get__(self, obj, objtype=None) -> any:
        return self if obj is None else self.fget(obj)

    def __set_name__(self, owner: Type["Stats"], name: str) -> None:
        super().__set_name__(owner, name)

        if not hasattr(owner, "properties"):
            owner.properties = []

        if name not in owner.properties:
            owner.properties.append(name)


class filterableproperty(_textstatproperty):
    def __get__(self, obj, objtype=None) -> any:
        if obj is not None:
            return self.fget(obj)

        return make_comparable(self.fget.__name__, objtype)


class filterabletextproperty(filterableproperty, textproperty): ...
