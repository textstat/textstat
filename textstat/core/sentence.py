from __future__ import annotations

import re

from textstat.core import mixins
from textstat.properties import filterableproperty


class Sentence(mixins.Span, mixins.Stats):
    regex = re.compile(r"\b[^.!?]+[.!?]+", re.UNICODE)

    @filterableproperty
    def length(self) -> int:
        return len(self.words)
