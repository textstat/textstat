from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, variant, expected",
    [
        (resources.EMPTY_STR, "en_US", 1, 0.0),
        (resources.EMPTY_STR, "en_US", 2, 0.0),
        (resources.EMPTY_STR, "en_US", 2, 0.0),
        (resources.EASY_TEXT, "en_US", 1, 1.359),
        (resources.EASY_TEXT, "en_US", 2, 1.754),
        (resources.EASY_TEXT, "en_US", 3, 2.396),
        (resources.EASY_TEXT, "en_US", 4, 2.36),
        (resources.SHORT_TEXT, "en_US", 1, 3.809),
        (resources.PUNCT_TEXT, "en_US", 1, 1.541),
        (resources.LONG_TEXT, "en_US", 1, 5.256),
        (resources.GERMAN_SAMPLE_A, "de_DE", 1, 3.77),
        (resources.GERMAN_SAMPLE_B, "de_DE", 1, 13.913),
    ],
)
def test_wiener_sachtextformel(
    text: str, lang: str, variant: int, expected: float
) -> None:
    assert round(metrics.wiener_sachtextformel(text, variant, lang), 3) == expected
