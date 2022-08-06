from textstat.core import Sentence


def test_sentence_length():
    sentence = Sentence("The quick brown fox jumps over the lazy dog.")

    sentence.length == 9


def test_sentence_equal_to_string():
    sentence = Sentence("The quick brown fox jumps over the lazy dog.")

    assert sentence == "The quick brown fox jumps over the lazy dog."
    assert "The quick brown fox jumps over the lazy dog." == sentence
