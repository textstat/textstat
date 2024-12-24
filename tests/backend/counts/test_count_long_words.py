from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "test,expected",
    [
        (resources.EASY_TEXT, 13),
        (resources.SHORT_TEXT, 1),
        (resources.PUNCT_TEXT, 7),
        (resources.LONG_TEXT, 77),
    ],
)
def test_count_long_words(test: str, expected: int) -> None:
    assert counts.count_long_words(test) == expected
