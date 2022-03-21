from textstat_en import Text


def test_reading_time(test_text):
    text = Text(test_text["text"])

    assert text.reading_time == test_text["statistics"]["reading_time"]
