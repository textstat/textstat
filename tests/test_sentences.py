from textstat import Sentence


def test_sentence_length():
    sentence = Sentence("The quick brown fox jumps over the lazy dog.")

    sentence.length == 9
