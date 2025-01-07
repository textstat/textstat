from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 0.111),
        (resources.SHORT_TEXT, 0.2),
        (resources.PUNCT_TEXT, 0.094),
        (resources.LONG_TEXT, 0.046),
    ],
)
def test_sentences_per_word(text: str, expected: float) -> None:
    assert round(metrics.sentences_per_word(text), 3) == expected
