from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 1.182),
        (resources.SHORT_TEXT, 1.0),
        (resources.PUNCT_TEXT, 1.4),
        (resources.LONG_TEXT, 4.529),
    ],
)
def test_rix(text: str, expected: float) -> None:
    assert round(metrics.rix(text), 3) == expected
