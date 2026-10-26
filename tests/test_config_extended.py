"""Extended coverage for textstat's global configuration.

``textstat`` is a module-level singleton, so every test here restores
the configuration it changes (rounding points, language, apostrophe
handling) in a finally block or via the autouse fixture below. All
behaviour below was verified by a probe script against the cloned
source.

Quirks pinned as-is:
- ``set_lang`` accepts any string without validation; an unknown locale
  only fails later, when a syllable lookup raises ``KeyError``.
- ``set_rounding_points`` accepts any value without validation; a
  non-integer only fails later inside ``_legacy_round`` (TypeError).
"""

import pytest

from textstat import textstat


@pytest.fixture(autouse=True)
def _restore_config():
    yield
    textstat.set_rounding_points(None)
    textstat.set_lang("en_US")
    textstat.set_rm_apostrophe(True)


LONG = (
    "The history of the Roman Empire is a long and complex story. "
    "Many scholars have studied its rise and its eventual decline over centuries. "
    "Trade networks connected distant provinces and carried goods, ideas, and people."
)


# ---------------------------------------------------------------- rounding


def test_set_rounding_points_rounds_metric_outputs():
    textstat.set_rounding_points(2)
    assert textstat.coleman_liau_index(LONG) == 11.33
    assert textstat.flesch_reading_ease(LONG) == 45.13


def test_set_rounding_points_none_restores_full_precision():
    textstat.set_rounding_points(2)
    assert textstat.coleman_liau_index(LONG) == 11.33
    textstat.set_rounding_points(None)
    assert textstat.coleman_liau_index(LONG) == pytest.approx(11.325714285714284)


def test_legacy_round_follows_rounding_points():
    assert textstat._legacy_round(1.23456) == 1.23456
    textstat.set_rounding_points(2)
    assert textstat._legacy_round(1.23456) == 1.23


def test_legacy_round_points_argument_warns_but_is_ignored():
    textstat.set_rounding_points(2)
    with pytest.warns(DeprecationWarning):
        assert textstat._legacy_round(1.23456, 5) == 1.23


def test_set_rounding_deprecated_wrapper():
    with pytest.warns(DeprecationWarning):
        textstat.set_rounding(True, points=1)
    assert textstat.coleman_liau_index(LONG) == 11.3
    with pytest.warns(DeprecationWarning):
        textstat.set_rounding(False)
    assert textstat.coleman_liau_index(LONG) == pytest.approx(11.325714285714284)


def test_set_rounding_points_accepts_anything_then_fails_late():
    assert textstat.set_rounding_points("x") is None
    with pytest.raises(TypeError):
        textstat._legacy_round(1.23456)


# ---------------------------------------------------------------- apostrophe handling


def test_set_rm_apostrophe_controls_contraction_handling():
    textstat.set_rm_apostrophe(True)
    assert textstat.remove_punctuation("don't stop") == "dont stop"
    textstat.set_rm_apostrophe(False)
    assert textstat.remove_punctuation("don't stop") == "don't stop"


# ---------------------------------------------------------------- language


def test_set_lang_spanish_changes_syllable_counting():
    textstat.set_lang("es_ES")
    assert textstat.syllable_count("hola mundo") == 4
    textstat.set_lang("en_US")
    assert textstat.syllable_count("hello world") == 3


def test_set_lang_unknown_locale_fails_only_on_use():
    assert textstat.set_lang("xx_XX") is None
    with pytest.raises(KeyError):
        textstat.syllable_count("hello world")


# ---------------------------------------------------------------- deprecations


def test_cache_clear_warns_and_does_nothing():
    with pytest.warns(DeprecationWarning):
        assert textstat._cache_clear() is None
