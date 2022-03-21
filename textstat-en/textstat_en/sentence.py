from textstat.sentence import Sentence as BaseSentence

from .word_collection import WordCollection


class Sentence(BaseSentence, WordCollection):
    ...
