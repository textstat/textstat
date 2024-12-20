from __future__ import annotations

from functools import lru_cache
import math
from typing import Callable, ParamSpec, TypeVar
import pkg_resources
import warnings
from pyphen import Pyphen  # type: ignore

LANG_CONFIGS: dict[str, dict[str, float]] = {
    "en": {  # Default config
        "fre_base": 206.835,
        "fre_sentence_length": 1.015,
        "fre_syll_per_word": 84.6,
        "syllable_threshold": 3,
    },
    "de": {
        # Toni Amstad
        "fre_base": 180,
        "fre_sentence_length": 1,
        "fre_syll_per_word": 58.5,
    },
    "es": {
        # Fernandez Huerta Readability Formula
        "fre_base": 206.84,
        "fre_sentence_length": 1.02,
        "fre_syll_per_word": 60.0,
    },
    "fr": {
        "fre_base": 207,
        "fre_sentence_length": 1.015,
        "fre_syll_per_word": 73.6,
    },
    "it": {
        # Flesch-Vacca
        "fre_base": 217,
        "fre_sentence_length": 1.3,
        "fre_syll_per_word": 60.0,
    },
    "nl": {
        # Flesch-Douma
        "fre_base": 206.835,
        "fre_sentence_length": 0.93,
        "fre_syll_per_word": 77,
    },
    "pl": {
        "syllable_threshold": 4,
    },
    "ru": {
        "fre_base": 206.835,
        "fre_sentence_length": 1.3,
        "fre_syll_per_word": 60.1,
    },
    "hu": {
        "fre_base": 206.835,
        "fre_sentence_length": 1.015,
        "fre_syll_per_word": 58.5,
        "syllable_threshold": 5,
    },
}

CACHE_SIZE = 128

P = ParamSpec("P")
T = TypeVar("T")


def typed_cache[**P, T](func: Callable[P, T]) -> Callable[P, T]:
    """Decorator to cache function results without losing type info"""
    return lru_cache(maxsize=CACHE_SIZE)(func)  # type: ignore


def get_grade_suffix(grade: int) -> str:
    """
    Select correct ordinal suffix
    """
    ordinal_map = {1: "st", 2: "nd", 3: "rd"}
    teens_map = {11: "th", 12: "th", 13: "th"}
    return teens_map.get(grade % 100, ordinal_map.get(grade % 10, "th"))


def get_lang_cfg(lang: str, key: str) -> float:
    """Read as get lang config"""
    lang_root = get_lang_root(lang)
    default = LANG_CONFIGS["en"]
    config = LANG_CONFIGS.get(lang_root, default)
    val = config.get(key, default.get(key))
    if val is None:
        raise ValueError(f"Unknown config key {key}")
    return val


def get_lang_root(lang: str) -> str:
    """Get the root of a language. For example, "en_US" returns "en". If the language is already
    the root, it is returned as is (e.g. "en").
    """
    if "_" in lang:
        return lang.split("_")[0]
    return lang


@typed_cache
def get_lang_easy_words(lang: str) -> set[str]:
    lang_root = get_lang_root(lang)
    try:
        return {
            ln.decode("utf-8").strip()
            for ln in pkg_resources.resource_stream(
                "textstat",
                f"resources/{lang_root}/easy_words.txt",
            )
        }
    except FileNotFoundError:
        warnings.warn(
            "There is no easy words vocabulary for " f"{lang_root}, using english.",
            Warning,
        )
        return {
            ln.decode("utf-8").strip()
            for ln in pkg_resources.resource_stream(
                "textstat", "resources/en/easy_words.txt"
            )
        }


@typed_cache
def get_pyphen(lang: str) -> Pyphen:
    return Pyphen(lang=lang)


def syllables_in_word(word: str, lang: str) -> int:
    """Count the number of syllables in a word"""
    return len(get_pyphen(lang).positions(word)) + 1  # type: ignore


def legacy_round(number: float, points: int) -> float:
    """Round `number`, unless the attribute `__round_outputs` is `False`.

    Round floating point outputs for backwards compatibility.
    Rounding can be turned off by setting the instance attribute
    `__round_outputs` to False.

    Parameters
    ----------
    number : float
    points : int, optional
        The number of decimal digits to return. If the instance attribute
        `__round_points` is not None, the value of `__round_point` will
        override the value passed for `points`. The default is 0.

    Returns
    -------
    float

    """
    return round(number, points)
