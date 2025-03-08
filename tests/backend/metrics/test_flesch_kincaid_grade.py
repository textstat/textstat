from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 4.488),
        (resources.SHORT_TEXT, "en_US", 2.88),
        (resources.PUNCT_TEXT, "en_US", 4.574),
        (resources.LONG_TEXT, "en_US", 10.359),
    ],
)
def test_flesch_kincaid_grade(text: str, lang: str, expected: float) -> None:
    assert round(metrics.flesch_kincaid_grade(text, lang), 3) == expected
