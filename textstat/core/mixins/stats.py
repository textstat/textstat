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
    """Base class providing statistical properties and methods for text analysis.

    This class serves as a foundation for text, sentence, and word analysis,
    providing properties for counting elements (letters, characters, words, etc.)
    and methods for computing averages and statistics.

    Attributes:
        properties: List of property names that are tracked for statistics.
    """

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
        """The original text string.

        Returns:
            The text string that this object was initialized with.
        """
        return self.__text

    @textproperty
    def letters(self) -> list[str]:
        """A list of all letter characters in the text (excluding whitespace).

        Returns:
            List of individual letter characters (Unicode category starting with 'L').
        """
        return [
            *(
                character
                for character in self.characters
                if category(character).startswith("L")
            )
        ]

    @textproperty
    def characters(self) -> list[str]:
        """A list of all characters in the text, excluding whitespace.

        Returns:
            List of individual characters with whitespace removed.
        """
        return [*"".join(self.text.split())]

    def avg(self, attribute: str, per: Optional[str] = None) -> float:
        """Calculate the average of one attribute per another attribute.

        Useful for computing ratios like average words per sentence or
        average syllables per word.

        Args:
            attribute: The attribute to measure (e.g., 'words', 'syllables').
            per: The attribute to divide by (e.g., 'sentences', 'words').
                If None, returns the count or length of the attribute.

        Returns:
            The average value as a float. Returns 0.0 if division by zero occurs.

        Examples:
            >>> text.avg("words", per="sentences")  # Average words per sentence
            >>> text.avg("syllables", per="words")  # Average syllables per word
        """
        try:
            attribute = getattr(self, attribute)
            per = getattr(self, per)
            return (attribute if isinstance(attribute, int) else len(attribute)) / (
                per if isinstance(per, int) else len(per)
            )
        except ZeroDivisionError:
            return 0.0

    def stats(self) -> dict[str, int]:
        """Get a dictionary of basic statistics for all tracked properties.

        Returns:
            Dictionary mapping property names to their counts (lengths).

        Examples:
            >>> text.stats()
            {'words': 42, 'sentences': 3, 'letters': 189, ...}
        """
        return {prop: len(getattr(self, prop)) for prop in self.__class__.properties}

    def stats_full(self) -> dict[str, int]:
        """Get a comprehensive dictionary of statistics including unique counts.

        Returns:
            Dictionary containing counts for properties, unique properties,
            and count properties (frequency counts).

        Examples:
            >>> text.stats_full()
            {'words': 42, 'unique_words': 35, 'word_count': {...}, ...}
        """
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
