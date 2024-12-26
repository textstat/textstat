from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 3.575),
        (resources.SHORT_TEXT, 4.62),
        (resources.PUNCT_TEXT, 5.82),
        (resources.LONG_TEXT, 11.408),
    ],
)
def test_automated_readability_index(text: str, expected: float) -> None:
    assert round(metrics.automated_readability_index(text), 3) == expected
