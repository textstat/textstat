import pytest
from textstat.backend import utils


@pytest.mark.parametrize(
    "grade, expected",
    [
        (1, "st"),
        (2, "nd"),
        (3, "rd"),
        (4, "th"),
        (5, "th"),
        (6, "th"),
        (7, "th"),
        (8, "th"),
        (9, "th"),
        (10, "th"),
        (11, "th"),
        (12, "th"),
        (13, "th"),
        (14, "th"),
        (15, "th"),
        (16, "th"),
        (17, "th"),
        (20, "th"),
        (21, "st"),
        (101, "st"),
        (4232, "nd"),
        (423, "rd"),
    ],
)
def test_get_grade_suffix(grade: int, expected: str) -> None:
    assert utils.get_grade_suffix(grade) == expected


@pytest.mark.parametrize(
    "lang, key, value",
    [
        (lang, key, utils.LANG_CONFIGS[lang][key])
        for lang in utils.LANG_CONFIGS
        for key in utils.LANG_CONFIGS[lang]
    ],
)
def test_get_lang_cfg(lang: str, key: str, value: float) -> None:
    assert utils.get_lang_cfg(lang, key) == value


@pytest.mark.parametrize(
    "lang, root",
    [
        ("en_US", "en"),
        ("en", "en"),
        ("en_GB", "en"),
        ("de_DE", "de"),
        ("es_ES", "es"),
        ("fr_FR", "fr"),
    ],
)
def test_get_lang_root(lang: str, root: str) -> None:
    assert utils.get_lang_root(lang) == root


@pytest.mark.parametrize(
    "lang, n_words",
    [
        ("en", 2941),  # TODO: why this is 2941 not 2949???
        ("es", 20000),
        ("de", 2941),
        ("fr", 2941),
    ],
)
def test_get_lang_easy_words(lang: str, n_words: int) -> None:
    # TODO: catch and assert warning
    assert len(utils.get_lang_easy_words(lang)) == n_words


@pytest.mark.parametrize(
    "lang",
    [
        "en_US",
        "en",
        "es_ES",
        "es",
        "de_DE",
        "de",
        "fr_FR",
    ],
)
def test_get_pyphen(lang: str) -> None:
    assert isinstance(utils.get_pyphen(lang), utils.Pyphen)


@pytest.mark.parametrize(
    "word, lang, expected",
    [
        ("hello", "en_US", 2),
        ("hola", "es_ES", 2),
    ],
)
def test_syllables_in_word(word: str, lang: str, expected: int) -> None:
    assert utils.syllables_in_word(word, lang) == expected


@pytest.mark.parametrize(
    "number, points, expected",
    [
        (1.2343, 0, 1),
        (433.432, 1, 433.4),
        (43.434, 2, 43.43),
        (4.324, 3, 4.324),
        (5.287, 4, 5.287),
        (7.47283478237, 5, 7.47283),
        (3847.472834972, 6, 3847.472835),
    ],
)
def test_legacy_round(number: float, points: int, expected: float) -> None:
    assert utils.legacy_round(number, points) == expected
