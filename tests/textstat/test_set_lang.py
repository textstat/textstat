from __future__ import annotations

import pytest
from textstat import textstat
from ..backend import resources


@pytest.mark.parametrize(
    "text,lang,expected",
    [
        (resources.EASY_TEXT, "en_US", 139),
        (resources.EASY_TEXT, "en_GB", 139),
        (resources.EASY_TEXT, "en", 139),
        (resources.EASY_TEXT, "de_DE", 145),
        (resources.EASY_TEXT, "de", 145),
        (resources.LONG_SPANISH_TEXT, "es_ES", 306),
        (resources.EASY_TEXT, "fr_FR", 122),
        (resources.EASY_TEXT, "it_IT", 151),
        (resources.EASY_TEXT, "nl_NL", 147),
    ],
)
def test_set_lang(text: str, lang: str, expected: int) -> None:
    ts = type(textstat)()
    ts.set_lang(lang)
    assert ts.syllable_count(text) == expected
