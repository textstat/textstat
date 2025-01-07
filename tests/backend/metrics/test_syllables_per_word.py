from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 1.404),
        (resources.SHORT_TEXT, "en_US", 1.4),
        (resources.PUNCT_TEXT, "en_US", 1.358),
        (resources.LONG_TEXT, "en_US", 1.476),
    ],
)
def test_syllables_per_word(text: str, lang: str, expected: float) -> None:
    assert round(metrics.syllables_per_word(text, lang), 3) == expected
