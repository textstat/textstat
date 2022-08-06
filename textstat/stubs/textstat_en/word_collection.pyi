from textstat import core
from textstat_en.word import Word as Word
from typing import Any

class WordCollection(core.WordCollection):
    word_class: Any
    @property
    def reading_time(self) -> float: ...
    @property
    def syllables(self): ...
