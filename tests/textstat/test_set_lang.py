from __future__ import annotations

import pytest
from textstat import textstat
from ..backend import resources


@pytest.mark.parametrize(
    "lang,expected",
    [
        ("en_US", 139),
        ("en_GB", 139),
        ("en", 139),
        ("de_DE", 145),
        ("de", 145),
        ("es_ES", 172),
        ("fr_FR", 122),
        ("it_IT", 151),
        ("nl_NL", 147),
    ],
)
def test_set_lang(lang: str, expected: int) -> None:
    ts = type(textstat)()
    ts.set_lang(lang)
    assert ts.syllable_count(resources.EASY_TEXT) == expected
