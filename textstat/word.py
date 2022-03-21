from __future__ import annotations

from ._filtering import filterable
from .stats import Stats


class Word(Stats):
    properties: list[str] = Stats.properties + [
        "letters",
        "length",
    ]

    @filterable[int]
    @property
    def length(self) -> int:
        return len(self.letters)
