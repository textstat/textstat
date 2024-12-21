from __future__ import annotations

import pytest
from textstat.backend import validations


@pytest.mark.parametrize(
    "word, syllable_threshold, lang, expected",
    [
        ("hello", 2, "en", False),
        ("hello", 2, "en_US", False),
        ("marriage", 2, "en", False),
        ("fragile", 2, "en", True),
        ("readability", 2, "en", True),
        ("regardless", 2, "en", True),
    ],
)
def test_is_difficult_word(
    word: str, syllable_threshold: int, lang: str, expected: bool
) -> None:
    assert validations.is_difficult_word(word, syllable_threshold, lang) == expected
