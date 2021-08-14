
import collections


class Stats:
    properties = []

    def __new__(cls, *_):
        if cls is Stats:
            raise TypeError(
                "The `Stats` class provides no functionality, "
                "so must be subclassed."
            )
        return object.__new__(cls)

    def __init__(self, text):
        self.__text = text
        self.__add_unique_properties()
        self.__add_count_properties()

    @property
    def text(self):
        return self.__text

    def avg(self, attribute, per=None):
        try:
            return len(getattr(self, attribute)) / len(getattr(self, per))
        except ZeroDivisionError:
            return 0.0

    def raw_stats(self):
        return {
            prop: len(getattr(self, prop))
            for prop in self.__class__.properties
        }

    def raw_stats_full(self):
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
            setattr(
                self.__class__,
                "unique_" + prop,
                property(make_getter(prop))
            )

    def __add_count_properties(self):
        def make_getter(value):
            return lambda self: collections.Counter(getattr(self, value))

        for prop in self.__class__.properties:
            setattr(
                self.__class__,
                prop[:-1] + "_count",
                property(make_getter(prop))
            )
