from __future__ import annotations

import re

from textstat.core.mixins.stats import Stats
from textstat.properties import filterableproperty


class Word(Stats):
    """Represents a single word for analysis.

    A Word provides properties and statistics about individual words,
    including character counts, letter counts, and other word-level metrics.

    Attributes:
        regex: The regular expression pattern used to identify words.
            Matches word characters including apostrophes and hyphens.
    """

    # Important: the apostrophe (’) character is intentionally
    #  - don't change it to a single quote (').
    regex = re.compile(r"\b[\w\’\'\-]+\b", re.UNICODE)

    @filterableproperty
    def length(self) -> int:
        """The number of letters in the word.

        Returns the count of letter characters, which may differ from the
        total number of characters if the word contains punctuation or
        non-letter characters.

        Returns:
            Integer count of letter characters in this word.

        Examples:
            >>> word = Word("hello")
            >>> word.length
            5
        """
        return len(self.letters)
