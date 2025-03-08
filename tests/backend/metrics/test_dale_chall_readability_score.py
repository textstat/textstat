from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 7.592),
        (resources.SHORT_TEXT, "en_US", 13.358),
        (resources.PUNCT_TEXT, "en_US", 6.248),
        (resources.LONG_TEXT, "en_US", 8.5),
    ],
)
def test_dale_chall_readability_score(text: str, lang: str, expected: float) -> None:
    assert round(metrics.dale_chall_readability_score(text, lang), 3) == expected
