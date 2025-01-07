from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 6.794),
        (resources.SHORT_TEXT, "en_US", 7.043),
        (resources.PUNCT_TEXT, "en_US", 6.248),
        (resources.LONG_TEXT, "en_US", 7.566),
    ],
)
def test_dale_chall_readability_score_v2(text: str, lang: str, expected: float) -> None:
    assert round(metrics.dale_chall_readability_score_v2(text, lang), 3) == expected
