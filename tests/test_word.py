
from textstat_core.word import Word


def test_word_letters():
    word = Word("vehicle")

    assert word.letters == ["v", "e", "h", "i", "c", "l", "e"]


def test_word_length():
    word = Word("referee")

    assert word.length == 7
