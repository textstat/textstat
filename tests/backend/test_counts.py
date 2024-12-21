from __future__ import annotations

import pytest
from textstat.backend import counts

from . import resources


@pytest.mark.parametrize(
    "text,ignore_spaces,expected",
    [
        ("", True, 0),
        ("", False, 0),
        ("a", True, 1),
        ("a ", True, 1),
        ("a ", False, 2),
        ("a b", True, 2),
        ("a b", False, 3),
        ("a $!&#@*b", True, 8),
        ("a $!&#@*b", False, 9),
        (resources.LONG_TEXT, True, 1748),
        (resources.LONG_TEXT, False, 2123),
        (resources.EASY_HUNGARIAN_TEXT, True, 43),
        (resources.EASY_HUNGARIAN_TEXT, False, 54),
    ],
)
def test_char_count(text: str, ignore_spaces: bool, expected: int) -> None:
    assert counts.char_count(text, ignore_spaces) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),
        ("a", 1),
        ("a ", 1),
        ("a b", 2),
        ("They're here, and they're there.", 24),
        (
            """Who's there?I have no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            57,
        ),
        (resources.LONG_TEXT, 1686),
        (resources.EASY_HUNGARIAN_TEXT, 42),
    ],
)
def test_letter_count(text: str, expected: int) -> None:
    assert counts.letter_count(text) == expected


@pytest.mark.parametrize(
    "text,removepunct,n_words",
    [
        ("", True, 0),
        ("a", True, 1),
        ("a ", True, 1),
        ("a b", True, 2),
        ("They're here, and they're there.", True, 5),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            True,
            12,
        ),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            False,
            13,
        ),
        (resources.LONG_TEXT, True, 372),
        (resources.LONG_TEXT, False, 376),
    ],
)
def test_lexicon_count(text: str, removepunct: bool, n_words: int) -> None:
    assert counts.lexicon_count(text, removepunct) == n_words


@pytest.mark.parametrize(
    "text,max_size,expected",
    [
        ("", 1, 0),
        ("a", 1, 1),
        ("a ", 1, 1),
        ("a b", 1, 2),
        ("They're here, and they're there.", 1, 0),
        ("They're here, and they're there.", 2, 0),
        ("They're here, and they're there.", 3, 1),
        ("They're here, and they're there.", 4, 2),
        ("who is me man, I, ye rogue", 1, 1),
        ("who is me man, I, ye rogue", 2, 4),
        ("who is me man, I, ye rogue", 3, 6),
    ],
)
def test_miniword_count(text: str, max_size: int, expected: int) -> None:
    assert counts.miniword_count(text, max_size) == expected


@pytest.mark.parametrize(
    "text,lang,expected",
    [
        ("", "en_US", 0),
        ("a", "en_US", 1),
        ("a ", "en_US", 1),
        ("a b", "en_US", 2),
        ("Where the dog at?", "en_US", 4),
        ("This marriage is an agreement of convenience", "en_US", 11),
        (resources.LONG_TEXT, "en_US", 519),
    ],
)
def test_syllable_count(text: str, lang: str, expected: int) -> None:
    assert counts.syllable_count(text, lang) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        (resources.EASY_TEXT, 11),
        (resources.SHORT_TEXT, 1),
        (resources.PUNCT_TEXT, 5),
        (resources.LONG_TEXT, 17),
        (resources.LONG_RUSSIAN_TEXT_GUILLEMETS, 16),
        (resources.HARD_HUNGARIAN_TEXT, 3),
        (resources.HARD_ACADEMIC_HUNGARIAN_TEXT, 6),
    ],
)
def test_sentence_count(text: str, expected: int) -> None:
    assert counts.sentence_count(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        # TODO
    ],
)
def test_count_complex_arabic_words(text: str, expected: int) -> None:
    assert counts.count_complex_arabic_words(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        # TODO
    ],
)
def test_count_arabic_syllables(text: str, expected: int) -> None:
    assert counts.count_arabic_syllables(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        # TODO
    ],
)
def test_count_faseeh(text: str, expected: int) -> None:
    assert counts.count_faseeh(text) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        # TODO
    ],
)
def test_count_arabic_long_words(text: str, expected: int) -> None:
    assert counts.count_arabic_long_words(text) == expected


@pytest.mark.parametrize(
    "test,lang,expected",
    [
        (resources.EASY_TEXT, "en_US", 6),
        (resources.SHORT_TEXT, "en_US", 1),
        (resources.PUNCT_TEXT, "en_US", 5),
        (resources.LONG_TEXT, "en_US", 32),
    ],
)
def test_polysyllabcount(test: str, lang: str, expected: int) -> None:
    assert counts.polysyllabcount(test, lang) == expected


@pytest.mark.parametrize(
    "text,lang,syllable_threshold,expected",
    [
        (resources.EASY_TEXT, "en_US", 1, 11),
        (resources.EASY_TEXT, "en_US", 2, 5),
        (resources.EASY_TEXT, "en_US", 3, 0),
        (resources.SHORT_TEXT, "en_US", 2, 1),
        (resources.PUNCT_TEXT, "en_US", 2, 6),
        (resources.LONG_TEXT, "en_US", 2, 49),
    ],
)
def test_difficult_words(
    text: str, lang: str, syllable_threshold: int, expected: int
) -> None:
    assert counts.difficult_words(text, lang, syllable_threshold) == expected


@pytest.mark.parametrize(
    "test,expected",
    [
        (resources.EASY_TEXT, 13),
        (resources.SHORT_TEXT, 1),
        (resources.PUNCT_TEXT, 7),
        (resources.LONG_TEXT, 77),
    ],
)
def test_long_word_count(test: str, expected: int) -> None:
    assert counts.long_word_count(test) == expected


@pytest.mark.parametrize(
    "test,lang,expected",
    [
        (resources.EASY_TEXT, "en_US", 68),
        (resources.SHORT_TEXT, "en_US", 4),
        (resources.PUNCT_TEXT, "en_US", 42),
        (resources.LONG_TEXT, "en_US", 270),
    ],
)
def test_monosyllabcount(test: str, lang: str, expected: int) -> None:
    assert counts.monosyllabcount(test, lang) == expected
