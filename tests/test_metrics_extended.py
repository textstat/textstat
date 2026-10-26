"""Extended coverage for textstat's readability metrics.

The upstream suite covers each metric with a handful of fixed texts;
this file pins exact values for a second, longer passage, the empty
and short-text edges, and the metrics with no dedicated upstream test
at all (mcalpine_eflaw has no test file of its own). All expected
values were produced by a probe script against the cloned source with
the NLTK cmudict corpus installed.

Long passage (3 sentences, 41 words):
"The history of the Roman Empire is a long and complex story. Many
scholars have studied its rise and its eventual decline over
centuries. Trade networks connected distant provinces and carried
goods, ideas, and people."
"""

import pytest

from textstat import textstat

SAMPLE = "The quick brown fox jumps over the lazy dog. It was a bright day."
LONG = (
    "The history of the Roman Empire is a long and complex story. "
    "Many scholars have studied its rise and its eventual decline over centuries. "
    "Trade networks connected distant provinces and carried goods, ideas, and people."
)


# ---------------------------------------------------------------- syllable-based counts


def test_syllable_count():
    assert textstat.syllable_count(SAMPLE) == 16
    assert textstat.syllable_count("hello world") == 3
    assert textstat.syllable_count("") == 0


def test_poly_and_mono_syllable_counts():
    assert textstat.polysyllabcount(SAMPLE) == 0
    assert textstat.monosyllabcount(SAMPLE) == 12


def test_avg_syllables_per_word():
    assert textstat.avg_syllables_per_word(SAMPLE) == pytest.approx(1.1428571428571428)


# ---------------------------------------------------------------- character-based metrics (no cmudict needed)


def test_coleman_liau_and_automated_readability():
    assert textstat.coleman_liau_index(LONG) == pytest.approx(11.325714285714284)
    assert textstat.automated_readability_index(LONG) == pytest.approx(9.16447619047619)


def test_lix_and_rix():
    assert textstat.lix(LONG) == pytest.approx(45.95238095238095)
    assert textstat.rix(LONG) == 4.0


def test_osman_gulpease_gutierrez():
    assert textstat.osman(LONG) == pytest.approx(56.99016190476189)
    assert textstat.gulpease_index(LONG) == pytest.approx(62.142857142857146)
    assert textstat.gutierrez_polini(LONG) == pytest.approx(41.508095238095244)


def test_empty_text_metrics_are_zero():
    assert textstat.osman("") == 0.0
    assert textstat.gulpease_index("") == 0.0
    assert textstat.gutierrez_polini("") == 0.0
    assert textstat.mcalpine_eflaw("") == 0.0


# ---------------------------------------------------------------- syllable-based metrics


def test_flesch_pair():
    assert textstat.flesch_reading_ease(LONG) == pytest.approx(45.1304761904762)
    assert textstat.flesch_kincaid_grade(LONG) == pytest.approx(9.862857142857145)


def test_smog_and_gunning_fog():
    assert textstat.smog_index(LONG) == pytest.approx(11.855464076750408)
    assert textstat.gunning_fog(LONG) == pytest.approx(11.523809523809526)


def test_dale_chall_both_versions_agree_on_this_text():
    assert textstat.dale_chall_readability_score(LONG) == pytest.approx(10.531166666666667)
    assert textstat.dale_chall_readability_score_v2(LONG) == pytest.approx(10.531166666666667)


def test_crawford_fernandez_szigriszt():
    assert textstat.crawford(LONG) == pytest.approx(3.5158571428571426)
    assert textstat.fernandez_huerta(LONG) == pytest.approx(88.65428571428572)
    assert textstat.szigriszt_pazos(LONG) == pytest.approx(84.80833333333335)


def test_spache_float_and_int_forms():
    assert textstat.spache_readability(LONG) == pytest.approx(5.9239999999999995)
    assert textstat.spache_readability(LONG, float_output=False) == 5


def test_linsear_write_formula():
    assert textstat.linsear_write_formula(LONG) == pytest.approx(7.166666666666666)


def test_wiener_sachtextformel_variants():
    assert textstat.wiener_sachtextformel(LONG, variant=1) == pytest.approx(7.897666666666666)
    assert textstat.wiener_sachtextformel(LONG, variant=2) == pytest.approx(7.904761904761905)
    assert textstat.wiener_sachtextformel(LONG, variant=3) == pytest.approx(7.0341000000000005)


def test_mcalpine_eflaw_has_no_dedicated_upstream_test():
    assert textstat.mcalpine_eflaw(LONG) == pytest.approx(15.333333333333334)
    assert textstat.mcalpine_eflaw(SAMPLE) == 11.0
    assert textstat.mcalpine_eflaw("Hi.") == 2.0


# ---------------------------------------------------------------- composite helpers


def test_text_standard_string_and_float_forms():
    assert textstat.text_standard(LONG) == "10th and 11th grade"
    assert textstat.text_standard(LONG, float_output=True) == 11.0


def test_text_standard_degenerate_inputs():
    assert textstat.text_standard("") == "0th and 1st grade"
    assert textstat.text_standard("Hi.") == "0th and 1st grade"


def test_reading_time():
    assert textstat.reading_time(LONG) == pytest.approx(2.70296)
    assert textstat.reading_time("") == 0.0
    assert textstat.reading_time(LONG, ms_per_char=10.0) == pytest.approx(1.84)


def test_difficult_words_count_and_list():
    assert textstat.difficult_words(LONG) == 14
    # Order is hash-random (built from a set), so only the set is pinned.
    assert set(textstat.difficult_words_list(LONG)) == {
        "studied", "connected", "networks", "centuries", "scholars", "Roman",
        "provinces", "Empire", "carried", "eventual", "decline", "distant",
        "ideas", "complex",
    }


def test_is_difficult_and_is_easy_word():
    assert textstat.is_difficult_word("complex") is True
    assert textstat.is_difficult_word("cat") is False
    assert textstat.is_easy_word("cat") is True


# ---------------------------------------------------------------- Arabic counters on Latin input


def test_arabic_counters_on_latin_text():
    # Pinned as observed: the Arabic counters do not short-circuit on
    # non-Arabic input; the long-word/faseeh/complex counters are zero
    # while the syllable heuristic still returns a count.
    assert textstat.count_arabic_syllables("hello world") == 8
    assert textstat.count_complex_arabic_words("hello world") == 0
    assert textstat.count_faseeh("hello world") == 0
    assert textstat.count_arabic_long_words("hello world") == 0
