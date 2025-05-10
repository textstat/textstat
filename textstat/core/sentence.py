from __future__ import annotations

from textstat.core.span import Span
from textstat.core.stats import Stats
from textstat.filtering import filterable


class Sentence(Span, Stats):
    properties: list[str] = Span.properties + []

    @filterable
    @property
    def length(self) -> int:
        return len(self.words)
