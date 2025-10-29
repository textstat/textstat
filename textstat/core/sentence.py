from __future__ import annotations

import re

from textstat.core.mixins.span import Span
from textstat.core.mixins.stats import Stats
from textstat.core.word import Word
from textstat.properties import filterableproperty


class Sentence(Span, Stats):
    regex = re.compile(r"\b[^.!?]+[.!?]+", re.UNICODE)
    word_class = Word

    @filterableproperty
    def length(self) -> int:
        return len(self.words)
