from textstat.{{cookiecutter.language}}.sentence import Sentence
from textstat.{{cookiecutter.language}}.word_collection import WordCollection

from textstat import core


class Text(core.Text, WordCollection):
    sentence_class = Sentence
