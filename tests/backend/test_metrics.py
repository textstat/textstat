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
        (resources.LONG_TEXT, 22.118),
    ],
)
def test_avg_sentence_length(text: str, expected: float) -> None:
    assert round(metrics.avg_sentence_length(text), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 9.0),
        (resources.SHORT_TEXT, 5.0),
        (resources.PUNCT_TEXT, 10.6),
        (resources.LONG_TEXT, 22.118),
    ],
)
def test_words_per_sentence(text: str, expected: float) -> None:
    # TODO: this is honestly the same as the other func, that should be looked into
    assert round(metrics.words_per_sentence(text), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 1.374),
        (resources.SHORT_TEXT, "en_US", 1.4),
        (resources.PUNCT_TEXT, "en_US", 1.358),
        (resources.LONG_TEXT, "en_US", 1.38),
    ],
)
def test_avg_syllables_per_word(text: str, lang: str, expected: float) -> None:
    assert round(metrics.avg_syllables_per_word(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 4.354),
        (resources.SHORT_TEXT, 5.0),
        (resources.PUNCT_TEXT, 4.66),
        (resources.LONG_TEXT, 4.649),
    ],
)
def test_avg_character_per_word(text: str, expected: float) -> None:
    assert round(metrics.avg_character_per_word(text), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 4.222),
        (resources.SHORT_TEXT, 4.8),
        (resources.PUNCT_TEXT, 4.283),
        (resources.LONG_TEXT, 4.484),
    ],
)
def test_avg_letter_per_word(text: str, expected: float) -> None:
    assert round(metrics.avg_letter_per_word(text), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 0.111),
        (resources.SHORT_TEXT, 0.2),
        (resources.PUNCT_TEXT, 0.094),
        (resources.LONG_TEXT, 0.045),
    ],
)
def test_avg_sentence_per_word(text: str, expected: float) -> None:
    assert round(metrics.avg_sentence_per_word(text), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 206.835),
        (resources.EASY_TEXT, "en_US", 81.482),
        (resources.SHORT_TEXT, "en_US", 83.32),
        (resources.PUNCT_TEXT, "en_US", 81.148),
        (resources.LONG_TEXT, "en_US", 67.611),
    ],
)
def test_flesch_reading_ease(text: str, lang: str, expected: float) -> None:
    assert round(metrics.flesch_reading_ease(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", -15.59),
        (resources.EASY_TEXT, "en_US", 4.13),
        (resources.SHORT_TEXT, "en_US", 2.88),
        (resources.PUNCT_TEXT, "en_US", 4.574),
        (resources.LONG_TEXT, "en_US", 9.324),
    ],
)
def test_flesch_kincaid_grade(text: str, lang: str, expected: float) -> None:
    assert round(metrics.flesch_kincaid_grade(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 7.348),
        (resources.SHORT_TEXT, "en_US", 0.0),
        (resources.PUNCT_TEXT, "en_US", 8.842),
        (resources.LONG_TEXT, "en_US", 11.088),
    ],
)
def test_smog_index(text: str, lang: str, expected: float) -> None:
    assert round(metrics.smog_index(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, -15.8),
        (resources.EASY_TEXT, 5.4),
        (resources.SHORT_TEXT, 6.12),
        (resources.PUNCT_TEXT, 6.249),
        (resources.LONG_TEXT, 8.869),
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
        (resources.LONG_TEXT, 11.525),
    ],
)
def test_automated_readability_index(text: str, expected: float) -> None:
    assert round(metrics.automated_readability_index(text), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", -1.0),
        (resources.EASY_TEXT, "en_US", 4.045),
        (resources.SHORT_TEXT, "en_US", 2.5),
        (resources.PUNCT_TEXT, "en_US", 5.3),
        (resources.LONG_TEXT, "en_US", 14.5),
    ],
)
def test_linsear_write_formula(text: str, lang: str, expected: float) -> None:
    assert round(metrics.linsear_write_formula(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 5.837),
        (resources.SHORT_TEXT, "en_US", 13.358),
        (resources.PUNCT_TEXT, "en_US", 6.844),
        (resources.LONG_TEXT, "en_US", 7.757),
    ],
)
def test_dale_chall_readability_score(text: str, lang: str, expected: float) -> None:
    assert round(metrics.dale_chall_readability_score(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 4.88),
        (resources.SHORT_TEXT, "en_US", 7.043),
        (resources.PUNCT_TEXT, "en_US", 5.95),
        (resources.LONG_TEXT, "en_US", 6.791),
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
        (resources.LONG_TEXT, "en_US", 10.762),
    ],
)
def test_gunning_fog(text: str, lang: str, expected: float) -> None:
    assert round(metrics.gunning_fog(text, lang), 3) == expected


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 26.172),
        (resources.SHORT_TEXT, 25.0),
        (resources.PUNCT_TEXT, 25.694),
        (resources.LONG_TEXT, 43.926),
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
        (resources.EASY_TEXT, "en_US", 2.542),
        (resources.SHORT_TEXT, "en_US", 3.264),
        (resources.PUNCT_TEXT, "en_US", 3.307),
        (resources.LONG_TEXT, "en_US", 5.078),
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
        (resources.EMPTY_STR, "en_US", 206.84),
        (resources.EASY_TEXT, "en_US", 115.236),
        (resources.SHORT_TEXT, "en_US", 117.74),
        (resources.PUNCT_TEXT, "en_US", 114.519),
        (resources.LONG_TEXT, "en_US", 101.461),
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
        (resources.LONG_TEXT, "en_US", 98.723),
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
        (resources.LONG_TEXT, 43.964),
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
        (resources.LONG_TEXT, "en_US", 2.43),
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
        (resources.LONG_TEXT, 62.067),
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
        (resources.LONG_TEXT, 56.074),
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
        (resources.LONG_TEXT, "en_US", 1, 4.829),
    ],
)
def test_wiener_sachtextformel(
    text: str, lang: str, variant: int, expected: float
) -> None:
    assert round(metrics.wiener_sachtextformel(text, variant, lang), 3) == expected
