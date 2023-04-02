from textstat.core import Word


def test_word_letters():
    word = Word("vehicle")

    assert word.letters == ["v", "e", "h", "i", "c", "l", "e"]


def test_word_length():
    word = Word("referee")

    assert word.length == 7


def test_word_equal_to_string():
    word = Word("factory")

    assert word == "factory"
    assert "factory" == word
