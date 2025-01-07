from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 4.222),
        (resources.SHORT_TEXT, 4.8),
        (resources.PUNCT_TEXT, 4.283),
        (resources.LONG_TEXT, 4.532),
    ],
)
def test_letters_per_word(text: str, expected: float) -> None:
    assert round(metrics.letters_per_word(text), 3) == expected
