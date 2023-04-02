import pytest

import textstat.en


@pytest.fixture
def example_sentence():
    return "when suddenly a White Rabbit with pink eyes ran close by her"


def test_words_with_more_than_two_syllables(example_sentence):
    text = textstat.en.Text(example_sentence)

    words = text.filter(textstat.en.Word.syllables > 2)

    assert words == [
        "suddenly",
    ]
