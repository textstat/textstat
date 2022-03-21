from __future__ import annotations

from ._filtering import filterable
from .word_collection import WordCollection


class Sentence(WordCollection):
    @filterable
    @property
    def length(self) -> int:
        return len(self.words)
