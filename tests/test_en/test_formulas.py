import pytest

from textstat.en import Text


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 85916),
        ("moby_dick", 52122),
        ("war_of_the_worlds", 31106),
    ],
)
def test_reading_time(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.reading_time == pytest.approx(expected, abs=1)


def test_sentence_reading_time():
    text = Text("This is an example sentence")
    assert text.reading_time == pytest.approx(1712, abs=1)


def test_reading_time_gets_shorter():
    test_text = "This is an example text. It will get shorter."

    first = Text(test_text).reading_time
    second = Text(test_text[:24]).reading_time

    assert first > second


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 75),
        ("moby_dick", 10),
        ("war_of_the_worlds", 61),
    ],
)
def test_flesch_reading_ease(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.flesch_reading_ease() == pytest.approx(expected, abs=1)


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 8),
        ("moby_dick", 24),
        ("war_of_the_worlds", 10),
    ],
)
def test_flesch_kincaid_grade(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.flesch_kincaid_grade() == pytest.approx(expected, abs=1)


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 6),
        ("moby_dick", 18),
        ("war_of_the_worlds", 9),
    ],
)
def test_smog(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.smog() == pytest.approx(expected, abs=1)


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 8),
        ("moby_dick", 20),
        ("war_of_the_worlds", 11),
    ],
)
def test_smog_grade(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.smog_grade() == pytest.approx(expected, abs=1)


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 6),
        ("moby_dick", 13),
        ("war_of_the_worlds", 9),
    ],
)
def test_coleman_liau_index(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.coleman_liau_index() == pytest.approx(expected, abs=1)


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 10),
        ("moby_dick", 29),
        ("war_of_the_worlds", 12),
    ],
)
def test_automated_readability_index(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.automated_readability_index() == pytest.approx(expected, abs=1)


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 13),
        ("moby_dick", 36),
        ("war_of_the_worlds", 14),
    ],
)
def test_linsear_write_formula(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.linsear_write_formula() == pytest.approx(expected, abs=1)


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 11),
        ("moby_dick", 28),
        ("war_of_the_worlds", 13),
    ],
)
def test_gunning_fog(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.gunning_fog() == pytest.approx(expected, abs=1)


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 36),
        ("moby_dick", 76),
        ("war_of_the_worlds", 43),
    ],
)
def test_lix(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.lix() == pytest.approx(expected, abs=1)


@pytest.mark.parametrize(
    "text_name,expected",
    [
        ("fairy_tales", 2),
        ("moby_dick", 12),
        ("war_of_the_worlds", 4.5),
    ],
)
def test_rix(all_test_texts, text_name, expected):
    text = Text(all_test_texts[text_name]["text"])
    assert text.rix() == pytest.approx(expected, abs=1)
