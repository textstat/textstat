from __future__ import annotations

from textstat.core.stats import Stats
from textstat.core.word_collection import WordCollection
from textstat.filtering import filterable


class Sentence(WordCollection, Stats):
    @filterable
    @property
    def length(self) -> int:
        return len(self.words)
