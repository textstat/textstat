from __future__ import annotations

import re

from textstat.core.mixins.stats import Stats
from textstat.properties import filterableproperty


class Word(Stats):
    regex = re.compile(r"\b[\w\’\'\-]+\b", re.UNICODE)

    @filterableproperty
    def length(self) -> int:
        return len(self.letters)
