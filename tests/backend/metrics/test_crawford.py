from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 1.195),
        (resources.SHORT_TEXT, "en_US", -0.647),
        (resources.PUNCT_TEXT, "en_US", 1.316),
        (resources.LONG_TEXT, "en_US", 2.888),
        (resources.LONG_SPANISH_TEXT, "es_ES", 5.089),
    ],
)
def test_crawford(text: str, lang: str, expected: float) -> None:
    assert round(metrics.crawford(text, lang), 3) == expected
