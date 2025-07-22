from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "lang,text,n_syllables,margin",
    [
        ("en_US", resources.SHORT_TEXT, 7, 0),
        ("en_US", resources.PUNCT_TEXT, 74, 2),
        ("en_US", "faeries", 2, 1),
        ("en_US", "relived", 2, 0),
        ("en_US", "couple", 2, 0),
        ("en_US", "enriched", 2, 0),
        ("en_US", "us", 1, 0),
        ("en_US", "too", 1, 0),
        ("en_US", "monopoly", 4, 0),
        ("en_US", "him", 1, 0),
        ("en_US", "he", 1, 0),
        ("en_US", "without", 2, 0),
        ("en_US", "creative", 3, 0),
        ("en_US", "every", 3, 0),
        ("en_US", "stimulating", 4, 0),
        ("en_US", "life", 1, 0),
        ("en_US", "cupboards", 2, 0),
        ("en_US", "day's", 1, 0),
        ("en_US", "forgotten", 3, 0),
        ("en_US", "through", 1, 0),
        ("en_US", "marriage", 2, 0),
        ("en_US", "hello", 2, 0),
        ("en_US", "the", 1, 0),
        ("en_US", "sentences", 3, 0),
        ("en_US", "songwriter", 3, 0),
        ("en_US", "removing", 3, 0),
        ("en_US", "interpersonal", 5, 0),
    ],
)
def test_syllable_count(lang: str, text: str, n_syllables: int, margin: int):
    """This test is formatted like this (checking margin rather than value)
    because the current return values are not always correct, so this form of
    checking tells us if the are within the expected margin of error rather
    than exactly the expected value.
    """
    count = counts.count_syllables(text, lang)
    diff = abs(count - n_syllables)
    assert diff <= margin


def test_count_syllables_with_unknown_word():
    """Test that count_syllables still produces an output when counting
    an unknown word.
    """
    assert counts.count_syllables("text_a", "en_US") == 2
