from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 110.363),
        (resources.SHORT_TEXT, "en_US", 114.615),
        (resources.PUNCT_TEXT, "en_US", 111.601),
        (resources.LONG_TEXT, "en_US", 93.01),
        (resources.LONG_SPANISH_TEXT, "es_ES", 62.162),
    ],
)
def test_szigriszt_pazos(text: str, lang: str, expected: float) -> None:
    assert round(metrics.szigriszt_pazos(text, lang), 3) == expected
