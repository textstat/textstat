from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 113.418),
        (resources.SHORT_TEXT, "en_US", 117.74),
        (resources.PUNCT_TEXT, "en_US", 114.519),
        (resources.LONG_TEXT, "en_US", 95.972),
        (resources.EMPTY_STR, "es_ES", 0.0),
        (resources.LONG_SPANISH_TEXT, "es_ES", 65.967),
    ],
)
def test_fernandez_huerta(text: str, lang: str, expected: float) -> None:
    assert round(metrics.fernandez_huerta(text, lang), 3) == expected
