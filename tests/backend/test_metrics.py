from __future__ import annotations

import pytest

from . import resources
from textstat.backend import metrics


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 9.0),
        (resources.SHORT_TEXT, 5.0),
        (resources.PUNCT_TEXT, 10.6),
        (resources.LONG_TEXT, 21.882),
    ],
)
def test_words_per_sentence(text: str, expected: float) -> None:
    assert round(metrics.words_per_sentence(text), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 1.374),
        (resources.SHORT_TEXT, "en_US", 1.4),
        (resources.PUNCT_TEXT, "en_US", 1.358),
        (resources.LONG_TEXT, "en_US", 1.395),
    ],
)
def test_avg_syllables_per_word(text: str, lang: str, expected: float) -> None:
    assert round(metrics.syllables_per_word(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 4.354),
        (resources.SHORT_TEXT, 5.0),
        (resources.PUNCT_TEXT, 4.66),
        (resources.LONG_TEXT, 4.699),
    ],
)
def test_avg_character_per_word(text: str, expected: float) -> None:
    assert round(metrics.chars_per_word(text), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 4.222),
        (resources.SHORT_TEXT, 4.8),
        (resources.PUNCT_TEXT, 4.283),
        (resources.LONG_TEXT, 4.532),
    ],
)
def test_avg_letter_per_word(text: str, expected: float) -> None:
    assert round(metrics.letters_per_word(text), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 0.111),
        (resources.SHORT_TEXT, 0.2),
        (resources.PUNCT_TEXT, 0.094),
        (resources.LONG_TEXT, 0.046),
    ],
)
def test_avg_sentence_per_word(text: str, expected: float) -> None:
    assert round(metrics.sentences_per_word(text), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 81.482),
        (resources.SHORT_TEXT, "en_US", 83.32),
        (resources.PUNCT_TEXT, "en_US", 81.148),
        (resources.LONG_TEXT, "en_US", 66.594),
        (resources.LONG_TEXT, "de_DE", 66.279),
        (resources.LONG_TEXT, "es_ES", 86.778),
        (resources.LONG_TEXT, "fr_FR", 82.303),
        (resources.LONG_TEXT, "it_IT", 91.617),
        (resources.LONG_TEXT, "nl_NL", 66.017),
        (resources.LONG_TEXT, "ru_RU", 118.288),
        (
            resources.EASY_HUNGARIAN_TEXT,
            "hu_HU",
            116.655,
        ),
        (resources.HARD_HUNGARIAN_TEXT, "hu_HU", 51.05),
        (resources.HARD_ACADEMIC_HUNGARIAN_TEXT, "hu_HU", 20.266),
    ],
)
def test_flesch_reading_ease(text: str, lang: str, expected: float) -> None:
    assert round(metrics.flesch_reading_ease(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 4.13),
        (resources.SHORT_TEXT, "en_US", 2.88),
        (resources.PUNCT_TEXT, "en_US", 4.574),
        (resources.LONG_TEXT, "en_US", 9.407),
    ],
)
def test_flesch_kincaid_grade(text: str, lang: str, expected: float) -> None:
    assert round(metrics.flesch_kincaid_grade(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 7.348),
        (resources.SHORT_TEXT, "en_US", 8.842),
        (resources.PUNCT_TEXT, "en_US", 8.842),
        (resources.LONG_TEXT, "en_US", 10.967),
        (resources.EASY_HUNGARIAN_TEXT, "hu_HU", 8.842),
        (resources.HARD_HUNGARIAN_TEXT, "hu_HU", 17.879),
        (resources.HARD_ACADEMIC_HUNGARIAN_TEXT, "hu_HU", 21.932),
    ],
)
def test_smog_index(text: str, lang: str, expected: float) -> None:
    assert round(metrics.smog_index(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 5.4),
        (resources.SHORT_TEXT, 6.12),
        (resources.PUNCT_TEXT, 6.249),
        (resources.LONG_TEXT, 9.134),
    ],
)
def test_coleman_liau_index(text: str, expected: float) -> None:
    assert round(metrics.coleman_liau_index(text), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 3.575),
        (resources.SHORT_TEXT, 4.62),
        (resources.PUNCT_TEXT, 5.82),
        (resources.LONG_TEXT, 11.643),
    ],
)
def test_automated_readability_index(text: str, expected: float) -> None:
    assert round(metrics.automated_readability_index(text), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 4.045),
        (resources.SHORT_TEXT, "en_US", 2.5),
        (resources.PUNCT_TEXT, "en_US", 5.3),
        (resources.LONG_TEXT, "en_US", 14.375),
    ],
)
def test_linsear_write_formula(text: str, lang: str, expected: float) -> None:
    assert round(metrics.linsear_write_formula(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 7.592),
        (resources.SHORT_TEXT, "en_US", 13.358),
        (resources.PUNCT_TEXT, "en_US", 6.248),
        (resources.LONG_TEXT, "en_US", 8.5),
    ],
)
def test_dale_chall_readability_score(text: str, lang: str, expected: float) -> None:
    assert round(metrics.dale_chall_readability_score(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 6.475),
        (resources.SHORT_TEXT, "en_US", 7.043),
        (resources.PUNCT_TEXT, "en_US", 5.95),
        (resources.LONG_TEXT, "en_US", 7.099),
    ],
)
def test_dale_chall_readability_score_v2(text: str, lang: str, expected: float) -> None:
    assert round(metrics.dale_chall_readability_score_v2(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 3.6),
        (resources.SHORT_TEXT, "en_US", 10.0),
        (resources.PUNCT_TEXT, "en_US", 7.259),
        (resources.LONG_TEXT, "en_US", 11.011),
        (
            resources.EASY_HUNGARIAN_TEXT,
            "hu_HU",
            4.8,
        ),  # TODO: why this one change so much (from 2.5)
        (resources.HARD_HUNGARIAN_TEXT, "hu_HU", 9.705),
        (resources.HARD_ACADEMIC_HUNGARIAN_TEXT, "hu_HU", 15.363),
    ],
)
def test_gunning_fog(text: str, lang: str, expected: float) -> None:
    assert round(metrics.gunning_fog(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 22.131),
        (resources.SHORT_TEXT, 25.0),
        (resources.PUNCT_TEXT, 23.808),
        (resources.LONG_TEXT, 42.581),
    ],
)
def test_lix(text: str, expected: float) -> None:
    assert round(metrics.lix(text), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 1.182),
        (resources.SHORT_TEXT, 1.0),
        (resources.PUNCT_TEXT, 1.4),
        (resources.LONG_TEXT, 4.529),
    ],
)
def test_rix(text: str, expected: float) -> None:
    assert round(metrics.rix(text), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 3.411),
        (resources.SHORT_TEXT, "en_US", 3.264),
        (resources.PUNCT_TEXT, "en_US", 3.307),
        (resources.LONG_TEXT, "en_US", 5.219),
    ],
)
def test_spache_readability(text: str, lang: str, expected: float) -> None:
    assert round(metrics.spache_readability(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 4.0),
        (resources.SHORT_TEXT, "en_US", 2.0),
        (resources.PUNCT_TEXT, "en_US", 6.0),
        (resources.LONG_TEXT, "en_US", 9.0),
    ],
)
def test_text_standard(text: str, lang: str, expected: float) -> None:
    assert round(metrics.text_standard(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, ms_per_char, expected",
    [
        (resources.EMPTY_STR, 0.0, 0.0),
        (resources.EMPTY_STR, 1.0, 0.0),
        (resources.EMPTY_STR, 5.3, 0.0),
        (resources.EASY_TEXT, 0.0, 0.0),
        (resources.EASY_TEXT, 0.4, 0.172),
        (resources.EASY_TEXT, 1.0, 0.431),
        (resources.SHORT_TEXT, 1.0, 0.025),
        (resources.SHORT_TEXT, 42.3, 1.058),
        (resources.PUNCT_TEXT, 40.0, 9.88),
        (resources.LONG_TEXT, 40.0, 69.92),
    ],
)
def test_reading_time(text: str, ms_per_char: float, expected: float) -> None:
    assert round(metrics.reading_time(text, ms_per_char), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 115.236),
        (resources.SHORT_TEXT, "en_US", 117.74),
        (resources.PUNCT_TEXT, "en_US", 114.519),
        (resources.LONG_TEXT, "en_US", 100.81),
        (resources.EMPTY_STR, "es_ES", 0.0),
        (resources.LONG_SPANISH_TEXT, "es_ES", 65.967),
    ],
)
def test_fernandez_huerta(text: str, lang: str, expected: float) -> None:
    assert round(metrics.fernandez_huerta(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 112.251),
        (resources.SHORT_TEXT, "en_US", 114.615),
        (resources.PUNCT_TEXT, "en_US", 111.601),
        (resources.LONG_TEXT, "en_US", 98.034),
        (resources.LONG_SPANISH_TEXT, "es_ES", 62.162),
    ],
)
def test_szigriszt_pazos(text: str, lang: str, expected: float) -> None:
    assert round(metrics.szigriszt_pazos(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 51.094),
        (resources.SHORT_TEXT, 46.89),
        (resources.PUNCT_TEXT, 49.945),
        (resources.LONG_TEXT, 43.578),
        (resources.EASY_SPANISH_TEXT, 64.35),
    ],
)
def test_gutierrez_polini(text: str, expected: float) -> None:
    assert round(metrics.gutierrez_polini(text), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 1.047),
        (resources.SHORT_TEXT, "en_US", -0.647),
        (resources.PUNCT_TEXT, "en_US", 1.316),
        (resources.LONG_TEXT, "en_US", 2.492),
        (resources.LONG_SPANISH_TEXT, "es_ES", 5.089),
    ],
)
def test_crawford(text: str, lang: str, expected: float) -> None:
    assert round(metrics.crawford(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 83.208),
        (resources.SHORT_TEXT, 84.483),
        (resources.PUNCT_TEXT, 76.427),
        (resources.LONG_TEXT, 61.056),
        (resources.HARD_ARABIC_TEXT, 39.292),
        (resources.EASY_ARABIC_TEXT, 102.186),
    ],
)
def test_osman(text: str, expected: float) -> None:
    assert round(metrics.osman(text), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 78.798),
        (resources.SHORT_TEXT, 99.0),
        (resources.PUNCT_TEXT, 70.698),
        (resources.LONG_TEXT, 55.72),
        (resources.ITALIAN_TEXT, 40.111),
    ],
)
def test_gulpease_index(text: str, expected: float) -> None:
    assert round(metrics.gulpease_index(text), 3) == expected


@pytest.mark.parametrize(
    "text, lang, variant, expected",
    [
        (resources.EMPTY_STR, "en_US", 1, 0.0),
        (resources.EMPTY_STR, "en_US", 2, 0.0),
        (resources.EMPTY_STR, "en_US", 2, 0.0),
        (resources.EASY_TEXT, "en_US", 1, 1.26),
        (resources.EASY_TEXT, "en_US", 2, 1.754),
        (resources.EASY_TEXT, "en_US", 3, 2.396),
        (resources.EASY_TEXT, "en_US", 4, 2.36),
        (resources.SHORT_TEXT, "en_US", 1, 3.809),
        (resources.PUNCT_TEXT, "en_US", 1, 1.844),
        (resources.LONG_TEXT, "en_US", 1, 4.76),
        (resources.GERMAN_SAMPLE_A, "de_DE", 1, 3.77),
        (resources.GERMAN_SAMPLE_B, "de_DE", 1, 13.913),
    ],
)
def test_wiener_sachtextformel(
    text: str, lang: str, variant: int, expected: float
) -> None:
    assert round(metrics.wiener_sachtextformel(text, variant, lang), 3) == expected
