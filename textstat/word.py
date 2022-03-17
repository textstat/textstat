from __future__ import annotations

from .stats import Stats


class Word(Stats):
    properties: list[str] = Stats.properties + [
        "letters",
        "length",
    ]

    def __repr__(self):
        return f"Word('{self.text}')"

    @property
    def length(self) -> int:
        return len(self.letters)
