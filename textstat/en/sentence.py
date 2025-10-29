from textstat import core
from textstat.en import mixins
from textstat.en.word import Word


class Sentence(core.Sentence, mixins.Span):
    word_class = Word
