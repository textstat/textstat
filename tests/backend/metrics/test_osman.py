from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 83.208),
        (resources.SHORT_TEXT, 84.483),
        (resources.PUNCT_TEXT, 76.427),
        (resources.LONG_TEXT, 61.056),
        (resources.HARD_ARABIC_TEXT, 39.292),
        (resources.EASY_ARABIC_TEXT, 102.186),
    ],
)
def test_osman(text: str, expected: float) -> None:
    assert round(metrics.osman(text), 3) == expected
