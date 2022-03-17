from __future__ import annotations

import re
from typing import Protocol

from .sentence import Sentence
from .word_collection import WordCollection


class __Readable(Protocol):
    def read(self) -> str:
        ...


class Text(WordCollection):
    properties: list[str] = WordCollection.properties + [
        "sentences",
    ]

    __sentence_regex = re.compile(r"\b[^.!?]+[.!?]+", re.UNICODE)

    @classmethod
    def load(cls, file_or_path: str | __Readable) -> Text:
        if hasattr(file_or_path, "read"):
            text: str = file_or_path.read()
        else:
            with open(file_or_path, "r") as f:
                text: str = f.read()

        return cls(text)

    @property
    def sentences(self) -> list[Sentence]:
        return [
            Sentence(sentence) for sentence in self.__sentence_regex.findall(self.text)
        ]
