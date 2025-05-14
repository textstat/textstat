from __future__ import annotations

from typing import TYPE_CHECKING

from textstat.core.word import Word
from textstat.properties import Comparison, textproperty

if TYPE_CHECKING:  # pragma: no cover
    from ..sentence import Sentence


class Span:
    """A span can be a paragraph, a sentence, or a whole text."""

    word_class = Word

    @textproperty
    def words(self) -> list[Word]:
        return [
            self.word_class(word) for word in self.word_class.regex.findall(self.text)
        ]

    def filter(self, comp: Comparison) -> list[Word | Sentence]:
        return [item for item in getattr(self, comp.type_name) if comp.compare(item)]

    def __iter__(self):
        return iter(self.words)
