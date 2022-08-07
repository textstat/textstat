import pytest

from textstat.en.word import Word


@pytest.mark.parametrize(
    "word,syllables",
    [
        ("solve", 1),
        ("drive", 1),
        ("float", 1),
        ("maid", 1),
        ("stage", 1),
        ("at", 1),
        ("cave", 1),
        ("hello", 2),
        ("despise", 2),
        ("polite", 2),
        ("frighten", 2),
        ("upset", 2),
        ("manage", 2),
        ("dividend", 3),
        ("communist", 3),
        ("exposure", 3),
        ("occupy", 3),
        ("champion", 3),
        ("addicted", 3),
        ("strikebreaker", 3),
        ("diplomatic", 4),
        ("stereotype", 4),
        ("celebration", 4),
        ("cemetery", 4),
        ("sensitivity", 5),
    ],
)
def test_syllable_count(word, syllables):
    word = Word(word)

    assert word.syllables == syllables
