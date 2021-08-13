import string
import collections


class Stats:
    properties = [
        "characters",
        "letters",
        "words",
        "syllables",
        "difficult_words"
    ]

    def __init__(self, text):
        self._text = text
        self._add_unique_properties()
        self._add_count_properties()

    @property
    def text(self):
        return self._text

    @property
    def characters(self):
        return [*self._text.replace(" ", "")]

    @property
    def letters(self):
        return [*(
            character for character in self.characters
            if character not in string.punctuation
        )]

    @property
    def words(self):
        return [*("".join(self.letters).lower().split())]

    @property
    def syllables(self):
        return []

    @property
    def difficult_words(self):
        return []

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

    def avg(self, attribute, per=None):
        try:
            return len(getattr(self, attribute)) / len(getattr(self, per))
        except ZeroDivisionError:
            return 0.0

    def _add_unique_properties(self):
        def make_getter(value):
            return lambda self: set(getattr(self, value))

        for prop in self.__class__.properties:
            setattr(
                self.__class__,
                "unique_" + prop,
                property(make_getter(prop))
            )

    def _add_count_properties(self):
        def make_getter(value):
            return lambda self: collections.Counter(getattr(self, value))

        for prop in self.__class__.properties:
            setattr(
                self.__class__,
                prop[:-1] + "_count",
                property(make_getter(prop))
            )
