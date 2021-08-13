
from textstat_core.statistics import Stats


def test_word_count(test_text):
    stats = Stats(test_text["text"])

    assert len(stats.words) == test_text["statistics"]["words"]
