from .word_collection import WordCollection


class Sentence(WordCollection):
    @property
    def length(self):
        return len(self.words)
