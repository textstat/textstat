from .word_collection import WordCollection

from ._filterable import filterable


class Sentence(WordCollection):
    @filterable
    @property
    def length(self) -> int:
        return len(self.words)
