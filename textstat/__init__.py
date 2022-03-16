import types

from textstat import stubs
from textstat.sentence import Sentence
from textstat.stats import Stats
from textstat.text import Text
from textstat.word import Word
from textstat.word_collection import WordCollection


def __try_import(lang) -> types.ModuleType:
    import importlib

    try:
        return importlib.import_module("textstat_en")
    except ImportError:
        pass


en: stubs.en = __try_import("en")
