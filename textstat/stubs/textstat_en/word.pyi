from textstat import core

class Word(core.Word):
    @property
    def syllables(self) -> int: ...
