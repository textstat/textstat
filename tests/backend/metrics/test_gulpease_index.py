from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 78.798),
        (resources.SHORT_TEXT, 99.0),
        (resources.PUNCT_TEXT, 70.698),
        (resources.LONG_TEXT, 56.22),
        (resources.ITALIAN_TEXT, 40.111),
    ],
)
def test_gulpease_index(text: str, expected: float) -> None:
    assert round(metrics.gulpease_index(text), 3) == expected
