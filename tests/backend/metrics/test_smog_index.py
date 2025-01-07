from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 7.348),
        (resources.SHORT_TEXT, "en_US", 8.842),
        (resources.PUNCT_TEXT, "en_US", 8.239),
        (resources.LONG_TEXT, "en_US", 11.67),
        (resources.EASY_HUNGARIAN_TEXT, "hu_HU", 8.842),
        (resources.HARD_HUNGARIAN_TEXT, "hu_HU", 17.879),
        (resources.HARD_ACADEMIC_HUNGARIAN_TEXT, "hu_HU", 21.932),
    ],
)
def test_smog_index(text: str, lang: str, expected: float) -> None:
    assert round(metrics.smog_index(text, lang), 3) == expected
