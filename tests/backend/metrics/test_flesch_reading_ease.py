from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 78.918),
        (resources.SHORT_TEXT, "en_US", 83.32),
        (resources.PUNCT_TEXT, "en_US", 81.148),
        (resources.LONG_TEXT, "en_US", 59.771),
        (resources.LONG_TEXT, "de_DE", 66.279),
        (resources.LONG_TEXT, "es_ES", 86.778),
        (resources.LONG_TEXT, "fr_FR", 82.303),
        (resources.LONG_TEXT, "it_IT", 91.617),
        (resources.LONG_TEXT, "nl_NL", 66.017),
        (resources.LONG_TEXT, "ru_RU", 118.288),
        (
            resources.EASY_HUNGARIAN_TEXT,
            "hu_HU",
            116.655,
        ),
        (resources.HARD_HUNGARIAN_TEXT, "hu_HU", 51.05),
        (resources.HARD_ACADEMIC_HUNGARIAN_TEXT, "hu_HU", 20.266),
    ],
)
def test_flesch_reading_ease(text: str, lang: str, expected: float) -> None:
    assert round(metrics.flesch_reading_ease(text, lang), 3) == expected
