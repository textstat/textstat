from __future__ import annotations

import pytest
from textstat import textstat
from ..backend import resources


@pytest.mark.parametrize(
    "lang,expected",
    [
        ("en_US", 1),
        ("en", 1),
        ("de_DE", 1),
        ("de", 1),
        ("es_ES", 1),
        ("fr_FR", 1),
        ("it_IT", 1),
        ("nl_NL", 1),
    ],
)
def test_set_lang(lang: str, expected: int) -> None:
    ts = type(textstat)()
    ts.set_lang(lang)
    assert ts.syllable_count(resources.EASY_TEXT) == expected
