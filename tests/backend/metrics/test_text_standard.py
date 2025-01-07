from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 4.0),
        (resources.SHORT_TEXT, "en_US", 2.0),
        (resources.PUNCT_TEXT, "en_US", 6.0),
        (resources.LONG_TEXT, "en_US", 11.0),
    ],
)
def test_text_standard(text: str, lang: str, expected: float) -> None:
    assert round(metrics.text_standard(text, lang), 3) == expected
