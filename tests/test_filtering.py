import pytest

from textstat import core


@pytest.fixture
def example_sentence():
    return "when suddenly a White Rabbit with pink eyes ran close by her"


def test_words_greater_than_six_letters(example_sentence):
    text = core.Text(example_sentence)

    words = text.filter(core.Word.length > 6)

    assert words == [
        "suddenly",
    ]


def test_words_less_than_six_letters(example_sentence):
    text = core.Text(example_sentence)

    words = text.filter(core.Word.length < 6)

    assert words == [
        "when",
        "a",
        "White",
        "with",
        "pink",
        "eyes",
        "ran",
        "close",
        "by",
        "her",
    ]


def test_words_less_than_or_equal_six_letters(example_sentence):
    text = core.Text(example_sentence)

    words = text.filter(core.Word.length <= 6)

    assert words == [
        "when",
        "a",
        "White",
        "Rabbit",
        "with",
        "pink",
        "eyes",
        "ran",
        "close",
        "by",
        "her",
    ]


def test_words_greater_than_or_equal_six_letters(example_sentence):
    text = core.Text(example_sentence)

    words = text.filter(core.Word.length >= 6)

    assert words == [
        "suddenly",
        "Rabbit",
    ]


def test_words_contain_ly(example_sentence):
    text = core.Text(example_sentence)

    words = text.filter(core.Word.text.contains("en"))

    assert words == ["when", "suddenly"]


def test_words_startswith_w(example_sentence):
    text = core.Text(example_sentence)

    words = text.filter(core.Word.text.startswith("w"))

    assert words == ["when", "with"]


def test_words_endswith_ly(example_sentence):
    text = core.Text(example_sentence)

    words = text.filter(core.Word.text.endswith("ly"))

    assert words == ["suddenly"]


def test_sentences_greater_than_four_words():
    text = core.Text(
        "Welcome to the Carpathians. I am anxiously expecting you. Sleep well to-night."
    )

    sentences = text.filter(core.Sentence.length > 4)

    assert sentences == ["I am anxiously expecting you."]


def test_sentences_ends_with_you():
    text = core.Text(
        "Welcome to the Carpathians. I am anxiously expecting you. Sleep well to-night."
    )

    sentences = text.filter(core.Sentence.text.endswith("you."))

    assert sentences == ["I am anxiously expecting you."]
