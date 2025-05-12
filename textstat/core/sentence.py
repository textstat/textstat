from __future__ import annotations

import re

from textstat.core.span import Span
from textstat.properties import filterableproperty


class Sentence(Span):
    regex = re.compile(r"\b[^.!?]+[.!?]+", re.UNICODE)

    @filterableproperty
    def length(self) -> int:
        return len(self.words)
