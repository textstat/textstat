from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 9.0),
        (resources.SHORT_TEXT, 5.0),
        (resources.PUNCT_TEXT, 10.6),
        (resources.LONG_TEXT, 21.882),
    ],
)
def test_words_per_sentence(text: str, expected: float) -> None:
    assert round(metrics.words_per_sentence(text), 3) == expected
