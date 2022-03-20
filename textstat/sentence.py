from .word_collection import WordCollection
from __future__ import annotations

from ._filtering import filterable


class Sentence(WordCollection):
    @filterable
    @property
    def length(self) -> int:
        return len(self.words)
