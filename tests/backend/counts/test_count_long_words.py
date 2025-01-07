from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "test, threshold, expected",
    [
        (resources.EASY_TEXT, 6, 13),
        (resources.SHORT_TEXT, 6, 1),
        (resources.SHORT_TEXT, 5, 1),
        (resources.SHORT_TEXT, 4, 1),
        (resources.PUNCT_TEXT, 6, 7),
        (resources.LONG_TEXT, 6, 77),
    ],
)
def test_count_long_words(test: str, threshold: int, expected: int) -> None:
    assert counts.count_long_words(test, threshold) == expected
