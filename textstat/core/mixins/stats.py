from __future__ import annotations

import collections
from typing import Optional
from unicodedata import category

from textstat.properties import filterableproperty, textproperty


class StatsMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        namespace = super().__prepare__(name, bases)
        namespace["properties"] = [
            *[*[prop for base in bases for prop in getattr(base, "properties", [])]]
        ]
        return namespace


class Stats(metaclass=StatsMeta):
    properties: list[str]

    def __new__(cls, *_):
        if cls is Stats:
            raise TypeError(
                "The `Stats` class provides no functionality, so must be subclassed."
            )
        return object.__new__(cls)

    def __init__(self, text):
        self.__text = text
        self.__add_unique_properties()
        self.__add_count_properties()

    @filterableproperty
    def text(self) -> str:
        return self.__text

    @textproperty
    def letters(self) -> list[str]:
        return [
            *(
                character
                for character in self.characters
                if category(character).startswith("L")
            )
        ]

    @textproperty
    def characters(self) -> list[str]:
        return [*"".join(self.text.split())]

    def avg(self, attribute: str, per: Optional[str] = None) -> float:
        try:
            attribute = getattr(self, attribute)
            per = getattr(self, per)
            return (attribute if isinstance(attribute, int) else len(attribute)) / (
                per if isinstance(per, int) else len(per)
            )
        except ZeroDivisionError:
            return 0.0

    def stats(self) -> dict[str, int]:
        return {prop: len(getattr(self, prop)) for prop in self.__class__.properties}

    def stats_full(self) -> dict[str, int]:
        return {
            prop: len(getattr(self, prop))
            for prop in [
                *self.__class__.properties,
                *["unique_" + u for u in self.__class__.properties],
                *[c[:-1] + "_count" for c in self.__class__.properties],
                # TODO: I think this getting the length of unique props and
                #  the length of the Counter for each prop is functionally
                #  equivilant, so maybe one of these can be removed?
            ]
        }

    def __add_unique_properties(self):
        def make_getter(value):
            return lambda self: set(getattr(self, value))

        for prop in self.__class__.properties:
            setattr(self.__class__, "unique_" + prop, property(make_getter(prop)))

    def __add_count_properties(self):
        def make_getter(value):
            return lambda self: collections.Counter(getattr(self, value))

        for prop in self.__class__.properties:
            count_name = prop[:-1] if prop.endswith("s") else prop
            setattr(self.__class__, count_name + "_count", property(make_getter(prop)))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, (str, self.__class__)):
            return self.text == other
        return super().__eq__(other)

    def __hash__(self) -> int:
        return hash(self.text)

    def __str__(self) -> str:
        return self.__text

    def __repr__(self) -> str:
        shown_text = self.text[:20] + "..." if len(self.text) > 20 else self.text
        return f"{self.__class__.__name__}('{shown_text}')"
