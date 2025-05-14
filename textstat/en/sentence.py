from textstat import core
from textstat.en import mixins


class Sentence(core.Sentence, mixins.Span):
    pass
