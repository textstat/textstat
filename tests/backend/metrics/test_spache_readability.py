from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 3.585),
        (resources.SHORT_TEXT, "en_US", 3.264),
        (resources.PUNCT_TEXT, "en_US", 3.469),
        (resources.LONG_TEXT, "en_US", 5.473),
    ],
)
def test_spache_readability(text: str, lang: str, expected: float) -> None:
    assert round(metrics.spache_readability(text, lang), 3) == expected
