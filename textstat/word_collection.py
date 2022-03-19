from __future__ import annotations

import re

from .stats import Stats
from .word import Word


class WordCollection(Stats):
    properties: list[str] = Stats.properties + [
        "words",
    ]

    __word_regex = re.compile(r"\b[\w\’\'\-]+\b", re.UNICODE)

    @property
    def words(self) -> list[Word]:
        return [Word(word) for word in self.__word_regex.findall(self.text)]

    def filter(self, comparison) -> list[Word]:
        return [
            item
            for item in getattr(self, comparison[0].__name__.lower() + "s")
            if getattr(getattr(item, comparison[1]), f"__{comparison[2]}__")(
                comparison[3]
            )
        ]
