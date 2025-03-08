from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 4.354),
        (resources.SHORT_TEXT, 5.0),
        (resources.PUNCT_TEXT, 4.66),
        (resources.LONG_TEXT, 4.649),
    ],
)
def test_chars_per_word(text: str, expected: float) -> None:
    assert round(metrics.chars_per_word(text), 3) == expected
