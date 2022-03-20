from __future__ import annotations

import re
from typing import TYPE_CHECKING

from ._filtering import Comparison
from .stats import Stats
from .word import Word

if TYPE_CHECKING:
    from .sentence import Sentence


class WordCollection(Stats):
    properties: list[str] = Stats.properties + [
        "words",
    ]

    __word_regex = re.compile(r"\b[\w\’\'\-]+\b", re.UNICODE)

    @property
    def words(self) -> list[Word]:
        return [Word(word) for word in self.__word_regex.findall(self.text)]

    def filter(self, comp: Comparison) -> list[Word | Sentence]:
        return [item for item in getattr(self, comp.type_name) if comp.compare(item)]
