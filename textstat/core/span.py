from __future__ import annotations

import re
from typing import TYPE_CHECKING

from textstat.core.stats import Stats
from textstat.core.word import Word
from textstat.filtering import Comparison

if TYPE_CHECKING:  # pragma: no cover
    from .sentence import Sentence


class Span(Stats):
    """A span can be a paragraph, a sentence, or a whole text."""

    word_class = Word
    properties: list[str] = Stats.properties + [
        "words",
    ]

    __word_regex = re.compile(r"\b[\w\’\'\-]+\b", re.UNICODE)

    @property
    def words(self) -> list[Word]:
        return [self.word_class(word) for word in self.__word_regex.findall(self.text)]

    def filter(self, comp: Comparison) -> list[Word | Sentence]:
        return [item for item in getattr(self, comp.type_name) if comp.compare(item)]

    def __iter__(self):
        return iter(self.words)
