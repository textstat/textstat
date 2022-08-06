from textstat import core
from textstat.filtering import filterable


class Word(core.Word):
    @filterable
    @property
    def syllables(self) -> int:
        ...
