from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 5.4),
        (resources.SHORT_TEXT, 6.12),
        (resources.PUNCT_TEXT, 6.249),
        (resources.LONG_TEXT, 9.134),
    ],
)
def test_coleman_liau_index(text: str, expected: float) -> None:
    assert round(metrics.coleman_liau_index(text), 3) == expected
