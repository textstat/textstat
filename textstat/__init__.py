import types
from typing import TYPE_CHECKING

from textstat import stubs


if TYPE_CHECKING:
    from textstat.sentence import Sentence
    from textstat.stats import Stats
    from textstat.text import Text
    from textstat.word import Word
    from textstat.word_collection import WordCollection


__LANG = "en"


def set_lang(lang: str):
    global __LANG
    __LANG = lang


def __getattr__(name: str):
    from textstat.sentence import Sentence  # noqa: F811
    from textstat.stats import Stats  # noqa: F811
    from textstat.text import Text  # noqa: F811
    from textstat.word import Word  # noqa: F811
    from textstat.word_collection import WordCollection  # noqa: F811

    default = locals()[name]

    if __try_import(__LANG) is None:
        return default

    if name in ["Sentence", "Stats", "Text", "Word", "WordCollection"]:
        return getattr(__try_import(__LANG), name)

    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")


def __try_import(lang) -> types.ModuleType:
    import importlib

    try:
        return importlib.import_module(f"textstat_{lang}")
    except ImportError:
        pass


en: stubs.en = __try_import("en")
