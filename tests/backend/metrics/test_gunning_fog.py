from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 4.004),
        (resources.SHORT_TEXT, "en_US", 10.0),
        (resources.PUNCT_TEXT, "en_US", 7.259),
        (resources.LONG_TEXT, "en_US", 11.441),
        (
            resources.EASY_HUNGARIAN_TEXT,
            "hu_HU",
            4.8,
        ),
        (resources.HARD_HUNGARIAN_TEXT, "hu_HU", 9.705),
        (resources.HARD_ACADEMIC_HUNGARIAN_TEXT, "hu_HU", 15.363),
    ],
)
def test_gunning_fog(text: str, lang: str, expected: float) -> None:
    assert round(metrics.gunning_fog(text, lang), 3) == expected
