from .word_collection import WordCollection


class Sentence(WordCollection):
    @property
    def length(self) -> int:
        return len(self.words)
