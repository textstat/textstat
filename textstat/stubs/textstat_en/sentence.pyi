from textstat import core
from textstat_en.word_collection import WordCollection as WordCollection

class Sentence(core.Sentence, WordCollection): ...
