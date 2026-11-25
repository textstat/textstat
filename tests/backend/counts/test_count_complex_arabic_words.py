from __future__ import annotations

import pytest
from textstat.backend import counts


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),
        (" \t\n", 0),
        ("مستشفياتهم", 0),
        ("مُسْتَشْفَيَاتُهُمْ", 1),  # six counted vowel marks; sukun is not counted
        ("(مُسْتَشْفَيَاتُهُمْ)،", 1),
        ("مُسْتَشْفَيَاتُهُمْ\nمُسْتَشْفَيَاتُهُمْ", 2),
        ("بَتَثَ جَحَخَ", 0),  # counts must not accumulate across words
        ("بْ" * 6, 0),  # sukun is outside the documented set of marks
    ],
)
@pytest.mark.parametrize("rm_apostrophe", [True, False])
def test_count_complex_arabic_words(
    text: str, expected: int, rm_apostrophe: bool
) -> None:
    assert counts.count_complex_arabic_words(text, rm_apostrophe) == expected


@pytest.mark.parametrize(
    "mark", ["\u064e", "\u064b", "\u064f", "\u064c", "\u0650", "\u064d", "\u0651"]
)
@pytest.mark.parametrize("count,expected", [(5, 0), (6, 1)])
def test_complex_word_threshold_for_each_mark(
    mark: str, count: int, expected: int
) -> None:
    assert counts.count_complex_arabic_words(("ب" + mark) * count) == expected


def test_public_complex_arabic_word_count() -> None:
    from textstat import textstat

    assert textstat.count_complex_arabic_words("مُسْتَشْفَيَاتُهُمْ") == 1
