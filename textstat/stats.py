from __future__ import annotations

import string
import collections


class Stats:
    properties: list[str] = ["letters", "characters"]

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

    @property
    def text(self) -> str:
        return self.__text

    @property
    def letters(self) -> list[str]:
        return [
            *(
                character
                for character in self.characters
                if character not in string.punctuation
            )
        ]

    @property
    def characters(self) -> list[str]:
        return [*self.text.replace(" ", "")]

    def avg(self, attribute, per=None) -> float:
        try:
            return len(getattr(self, attribute)) / len(getattr(self, per))
        except ZeroDivisionError:
            return 0.0

    def raw_stats(self) -> dict[str, int]:
        return {prop: len(getattr(self, prop)) for prop in self.__class__.properties}

    def raw_stats_full(self) -> dict[str, int]:
        return {
            prop: len(getattr(self, prop))
            for prop in [
                *self.__class__.properties,
                *["unique_" + u for u in self.__class__.properties],
                *[c[:-1] + "_count" for c in self.__class__.properties],
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
            setattr(self.__class__, prop[:-1] + "_count", property(make_getter(prop)))

    def __eq__(self, other: object) -> bool:
        if isinstance(other, str) or isinstance(other, self.__class__):
            return self.text == other
        return super().__eq__(other)
