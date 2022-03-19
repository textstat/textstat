from pathlib import Path
from textstat import Text


def test_word_count(test_text):
    text = Text(test_text["text"])

    assert len(text.words) == test_text["statistics"]["words"]


def test_character_count(test_text):
    text = Text(test_text["text"])

    assert len(text.characters) == test_text["statistics"]["characters"]


def test_letter_count(test_text):
    text = Text(test_text["text"])

    assert len(text.letters) == test_text["statistics"]["letters"]


def test_sentence_count(test_text):
    text = Text(test_text["text"])

    assert len(text.sentences) == test_text["statistics"]["sentences"]


def test_average_letter_per_word(test_text):
    text = Text(test_text["text"])

    stats = test_text["statistics"]

    actual = stats["letters"] / stats["words"]

    assert text.avg("letters", per="words") == actual


def test_average_character_per_word(test_text):
    text = Text(test_text["text"])

    stats = test_text["statistics"]

    actual = stats["characters"] / stats["words"]

    assert text.avg("characters", per="words") == actual


def test_blank_text_produces_zero_averages():
    text = Text("")

    assert text.avg("characters", per="words") == 0


def test_load_text_from_file_path(test_text_file: Path):
    text = Text.load(str(test_text_file))

    assert text.text == test_text_file.read_text()


def test_load_text_from_file(test_text_file: Path):
    with open(str(test_text_file), "r") as f:
        text = Text.load(f)

    assert text.text == test_text_file.read_text()


def test_text_equal_to_string(test_text):
    text = Text(test_text["text"])

    assert text == test_text["text"]
    assert test_text["text"] == text
