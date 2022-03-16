import re
import string

from .stats import Stats
from .word import Word


class WordCollection(Stats):
    properties = [
        "characters",
        "letters",
        "words",
    ]

    __word_regex = re.compile(r"\b[\w\’\'\-]+\b", re.UNICODE)

    @property
    def characters(self):
        return [*self.text.replace(" ", "")]

    @property
    def letters(self):
        return [
            *(
                character
                for character in self.characters
                if character not in string.punctuation
            )
        ]

    @property
    def words(self):
        return [Word(word) for word in self.__word_regex.findall(self.text)]
