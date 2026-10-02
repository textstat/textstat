from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 5.738),
        (resources.SHORT_TEXT, 6.504),
        (resources.PUNCT_TEXT, 6.592),
        (resources.LONG_TEXT, 9.497),
        (
            (
                "Readability formulas estimate how hard a passage is to read. "
                "Teachers often use them when choosing material for students. "
                "The Coleman-Liau index relies on characters instead of syllables."
            ),
            13.789,
        ),
    ],
)
def test_coleman_liau_index(text: str, expected: float) -> None:
    assert round(metrics.coleman_liau_index(text), 3) == expected

