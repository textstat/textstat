import pytest

from textstat.core.mixins import Stats


class Text(Stats): ...


def test_stats_cant_be_instantiated():
    with pytest.raises(TypeError):
        Stats("")


def test_stats_can_be_equal_to_string():
    assert Text("this is a test") == "this is a test"


def test_stats_can_be_equal_to_each_other():
    assert Text("this is a test") == Text("this is a test")


def test_stats_output():
    text = Text("this is a test?")

    assert text.stats() == {"characters": 12, "letters": 11}


def test_full_stats_output():
    text = Text("this is a test?")

    assert text.stats_full() == {
        "characters": 12,
        "letters": 11,
        "character_count": 7,
        "letter_count": 6,
        "unique_characters": 7,
        "unique_letters": 6,
    }

    text = Text("aaaaaaaaaa")

    assert text.stats_full() == {
        "characters": 10,
        "letters": 10,
        "character_count": 1,
        "letter_count": 1,
        "unique_characters": 1,
        "unique_letters": 1,
    }
