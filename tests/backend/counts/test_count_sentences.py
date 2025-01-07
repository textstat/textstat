from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "text,expected",
    [
        (resources.EMPTY_STR, 0),
        (resources.EASY_TEXT, 11),
        (resources.SHORT_TEXT, 1),
        (resources.PUNCT_TEXT, 5),
        (resources.LONG_TEXT, 17),
        (resources.LONG_RUSSIAN_TEXT_GUILLEMETS, 16),
        (resources.HARD_HUNGARIAN_TEXT, 3),
        (resources.HARD_ACADEMIC_HUNGARIAN_TEXT, 6),
    ],
)
def test_count_sentences(text: str, expected: int) -> None:
    assert counts.count_sentences(text) == expected
