from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "test,lang,expected",
    [
        (resources.EASY_TEXT, "en_US", 65),
        (resources.SHORT_TEXT, "en_US", 4),
        (resources.PUNCT_TEXT, "en_US", 41),
        (resources.LONG_TEXT, "en_US", 249),
    ],
)
def test_count_monosyllable_words(test: str, lang: str, expected: int) -> None:
    assert counts.count_monosyllable_words(test, lang) == expected
