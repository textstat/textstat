from __future__ import annotations

from textstat.core.stats import Stats
from textstat.filtering import filterable


class Word(Stats):
    properties: list[str] = Stats.properties + [
        "letters",
        "length",
    ]

    @filterable
    @property
    def length(self) -> int:
        return len(self.letters)
