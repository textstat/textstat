from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "text,lang,syllable_threshold,unique,expected",
    [
        (resources.EASY_TEXT, "en_US", 1, True, 11),
        (resources.EASY_TEXT, "en_US", 1, False, 22),
        (resources.EASY_TEXT, "en_US", 2, True, 6),
        (resources.EASY_TEXT, "en_US", 2, False, 17),
        (resources.EASY_TEXT, "en_US", 3, True, 1),
        (resources.SHORT_TEXT, "en_US", 2, True, 1),
        (resources.PUNCT_TEXT, "en_US", 2, True, 7),
        (resources.LONG_TEXT, "en_US", 2, True, 57),
    ],
)
def test_count_difficult_words(
    text: str, lang: str, syllable_threshold: int, unique: bool, expected: int
) -> None:
    assert (
        counts.count_difficult_words(text, lang, syllable_threshold, unique) == expected
    )
