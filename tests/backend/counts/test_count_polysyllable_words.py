from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "test,lang,expected",
    [
        (resources.EASY_TEXT, "en_US", 6),
        (resources.SHORT_TEXT, "en_US", 1),
        (resources.PUNCT_TEXT, "en_US", 4),
        (resources.LONG_TEXT, "en_US", 38),
    ],
)
def test_count_polysyllable_words(test: str, lang: str, expected: int) -> None:
    assert counts.count_polysyllable_words(test, lang) == expected
