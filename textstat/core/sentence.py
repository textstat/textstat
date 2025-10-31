from __future__ import annotations

import re

from textstat.core.mixins.span import Span
from textstat.core.mixins.stats import Stats
from textstat.core.word import Word
from textstat.properties import filterableproperty


class Sentence(Span, Stats):
    """Represents a single sentence for analysis.

    A Sentence extracts and provides statistics about words within a single
    sentence. It combines functionality from Span and Stats mixins to provide
    comprehensive sentence-level analysis.

    Attributes:
        regex: The regular expression pattern used to identify sentences.
        word_class: The class to use for creating Word objects.
    """

    regex = re.compile(r"\b[^.!?]+[.!?]+", re.UNICODE)
    word_class = Word

    @filterableproperty
    def length(self) -> int:
        """The number of words in the sentence.

        Returns:
            Integer count of words in this sentence.

        Examples:
            >>> sentence = Sentence("This is a test sentence.")
            >>> sentence.length
            5
        """
        return len(self.words)
