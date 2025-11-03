from __future__ import annotations

import re
from typing import Protocol

from textstat.core import mixins
from textstat.core.sentence import Sentence
from textstat.core.word import Word
from textstat.properties import textproperty


class __Readable(Protocol):  # pragma: no cover
    def read(self) -> str: ...


class Text(mixins.Stats, mixins.Span):
    """Represents a text document for analysis.

    The Text class provides methods for analyzing text at the document level,
    including extracting sentences and words, and computing various statistics.
    It combines functionality from Stats and Span mixins.

    Attributes:
        sentence_class: The class to use for creating Sentence objects.
        word_class: The class to use for creating Word objects.
    """

    sentence_class = Sentence
    word_class = Word

    __acronym_regex = re.compile(r"\b(?:[^\W\d_][\.]){2,}", re.UNICODE)

    @classmethod
    def load(cls, file_or_path: __Readable | str) -> Text:
        """Load text from a file or file-like object.

        Args:
            file_or_path: Either a file path (string) or a file-like object
                with a read() method. Files are opened with UTF-8 encoding
                (with BOM support via utf-8-sig).

        Returns:
            A Text instance containing the loaded text.

        Examples:
            >>> text = Text.load("document.txt")

            or:

            >>> with open("file.txt") as f:
            ...     text = Text.load(f)
        """
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
        """A list of all sentences found in the text.

        Sentences are extracted using the sentence_class regex pattern.
        Acronyms (e.g., "U.S.A.") are handled to avoid incorrect splitting.

        Returns:
            List of Sentence objects found in the text.
        """
        return [
            self.sentence_class(sentence)
            for sentence in self.sentence_class.regex.findall(
                self.__remove_acronyms(self.text)
            )
        ]
