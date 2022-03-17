from __future__ import annotations

import re

from .sentence import Sentence
from .word_collection import WordCollection


class Text(WordCollection):
    properties: list[str] = WordCollection.properties + [
        "sentences",
    ]

    __sentence_regex = re.compile(r"\b[^.!?]+[.!?]+", re.UNICODE)

    @property
    def sentences(self) -> list[Sentence]:
        return [
            Sentence(sentence) for sentence in self.__sentence_regex.findall(self.text)
        ]
