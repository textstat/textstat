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
