from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, ms_per_char, expected",
    [
        (resources.EMPTY_STR, 0.0, 0.0),
        (resources.EMPTY_STR, 1.0, 0.0),
        (resources.EMPTY_STR, 5.3, 0.0),
        (resources.EASY_TEXT, 0.0, 0.0),
        (resources.EASY_TEXT, 0.4, 0.172),
        (resources.EASY_TEXT, 1.0, 0.431),
        (resources.SHORT_TEXT, 1.0, 0.025),
        (resources.SHORT_TEXT, 42.3, 1.058),
        (resources.PUNCT_TEXT, 40.0, 9.88),
        (resources.LONG_TEXT, 40.0, 69.92),
    ],
)
def test_reading_time(text: str, ms_per_char: float, expected: float) -> None:
    assert round(metrics.reading_time(text, ms_per_char), 3) == expected
