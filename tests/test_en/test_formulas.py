from textstat_en import Text


def test_reading_time(test_text):
    text = Text(test_text["text"])

    assert text.reading_time == test_text["statistics"]["reading_time"]


def test_flesch_reading_ease(test_text):
    text = Text(test_text["text"])

    assert text.flesch_reading_ease() == 0


def test_flesch_kincaid_grade(test_text):
    text = Text(test_text["text"])

    assert text.flesch_kincaid_grade() == 0


def test_smog(test_text):
    text = Text(test_text["text"])

    assert text.smog() == 0


def test_smog_grade(test_text):
    text = Text(test_text["text"])

    assert text.smog_grade() == 0


def test_coleman_liau_index(test_text):
    text = Text(test_text["text"])

    assert text.coleman_liau_index() == 0


def test_linsear_write_formula(test_text):
    text = Text(test_text["text"])

    assert text.linsear_write_formula() == 0


def test_gunning_fog(test_text):
    text = Text(test_text["text"])

    assert text.gunning_fog() == 0


def test_lix(test_text):
    text = Text(test_text["text"])

    assert text.lix() == 0


def test_rix(test_text):
    text = Text(test_text["text"])

    assert text.rix() == 0
