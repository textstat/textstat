from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 4.886),
        (resources.SHORT_TEXT, "en_US", 4.556),
        (resources.PUNCT_TEXT, "en_US", 4.803),
        (resources.LONG_TEXT, "en_US", 6.214),
    ],
)
def test_powers_sumner_kearl(text: str, lang: str, expected: float) -> None:
    assert round(metrics.powers_sumner_kearl(text, lang), 3) == expected


def test_powers_sumner_kearl_formula() -> None:
    sentence_length = metrics.words_per_sentence(resources.LONG_TEXT)
    syllables = metrics.syllables_per_word(resources.LONG_TEXT, "en_US")
    expected = 0.0778 * sentence_length + 0.0455 * 100 * syllables - 2.2029
    assert metrics.powers_sumner_kearl(resources.LONG_TEXT, "en_US") == expected
