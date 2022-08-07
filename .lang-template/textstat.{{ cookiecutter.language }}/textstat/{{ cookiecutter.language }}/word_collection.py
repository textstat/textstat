from textstat_{{cookiecutter.language}}.word import Word

from textstat import core
from textstat.filtering import filterable


class WordCollection(core.WordCollection):
    word_class = Word

    @property
    def reading_time(self) -> float:
        ...

    @filterable
    @property
    def syllables(self):
        return sum(word.syllables for word in self.words)
