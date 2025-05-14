from __future__ import annotations

import re

from typing_extensions import Protocol

from textstat.core import mixins
from textstat.core.sentence import Sentence
from textstat.properties import textproperty


class __Readable(Protocol):  # pragma: no cover
    def read(self) -> str: ...


class Text(mixins.Stats, mixins.Span):
    sentence_class = Sentence

    __acronym_regex = re.compile(r"\b(?:[^\W\d_][\.]){2,}", re.UNICODE)

    @classmethod
    def load(cls, file_or_path: __Readable | str) -> Text:
        if hasattr(file_or_path, "read"):
            text: str = file_or_path.read()
        else:
            with open(file_or_path, "r", encoding="utf-8-sig") as f:
                text: str = f.read()

        return cls(text)

    def __remove_acronyms(self, text: str) -> str:
        for result in self.__acronym_regex.findall(text):
            text = text.replace(result, result.replace(".", ""))
        return text

    @textproperty
    def sentences(self) -> list[Sentence]:
        return [
            self.sentence_class(sentence)
            for sentence in self.sentence_class.regex.findall(
                self.__remove_acronyms(self.text)
            )
        ]
