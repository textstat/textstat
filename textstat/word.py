from __future__ import annotations

from .stats import Stats
from ._filterable import filterable


class Word(Stats):
    properties: list[str] = Stats.properties + [
        "letters",
        "length",
    ]

    def __repr__(self):
        return f"Word('{self.text}')"

    @filterable
    @property
    def length(self) -> int:
        return len(self.letters)
