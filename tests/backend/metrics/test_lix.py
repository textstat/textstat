from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 22.131),
        (resources.SHORT_TEXT, 25.0),
        (resources.PUNCT_TEXT, 23.808),
        (resources.LONG_TEXT, 42.581),
    ],
)
def test_lix(text: str, expected: float) -> None:
    assert round(metrics.lix(text), 3) == expected
