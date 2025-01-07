from __future__ import annotations

import pytest
from textstat.backend import validations
from .. import resources


@pytest.mark.parametrize(
    "word, syllable_threshold, lang, expected",
    [
        (resources.EMPTY_STR, 0, "en", False),
        (resources.EMPTY_STR, 1, "en", False),
        (resources.EASY_TEXT, 0, "en", False),
        (resources.EASY_WORD, 0, "en", False),
        (resources.DIFFICULT_WORD, 0, "en", True),
        (resources.DIFFICULT_WORD, 1, "en", True),
        (resources.DIFFICULT_WORD, 2, "en", True),
        (resources.DIFFICULT_WORD, 3, "en", True),
        (resources.DIFFICULT_WORD, 4, "en", False),
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
