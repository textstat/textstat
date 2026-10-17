import pytest
import textstat

@pytest.mark.parametrize("empty_input", ["", "   ", "\t\n", "  \n  "])
def test_empty_string_flesch_reading_ease(empty_input):
    assert textstat.flesch_reading_ease(empty_input) == 0.0

@pytest.mark.parametrize("empty_input", ["", "   ", "\t\n", "  \n  "])
def test_empty_string_syllable_count(empty_input):
    assert textstat.syllable_count(empty_input) == 0

def test_empty_string_all_metrics():
    blank = ""
    assert textstat.flesch_kincaid_grade(blank) == 0.0
    assert textstat.gunning_fog(blank) == 0.0
    assert textstat.automated_readability_index(blank) == 0.0
    assert textstat.lexicon_count(blank) == 0
    assert textstat.sentence_count(blank) == 0

import pytest
import textstat

@pytest.mark.parametrize("empty_input", ["", "   ", "\t\n", "  \n  "])
def test_empty_string_flesch_reading_ease(empty_input):
    assert textstat.flesch_reading_ease(empty_input) == 0.0

@pytest.mark.parametrize("empty_input", ["", "   ", "\t\n", "  \n  "])
def test_empty_string_syllable_count(empty_input):
    assert textstat.syllable_count(empty_input) == 0

def test_empty_string_all_metrics():
    blank = ""
    assert textstat.flesch_kincaid_grade(blank) == 0.0
    assert textstat.gunning_fog(blank) == 0.0
    assert textstat.automated_readability_index(blank) == 0.0
    assert textstat.lexicon_count(blank) == 0
    assert textstat.sentence_count(blank) == 0
