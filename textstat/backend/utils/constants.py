from __future__ import annotations
import typing

if typing.TYPE_CHECKING:
    import sys

    if sys.version_info < (3, 10):
        from typing_extensions import ParamSpec, TypeVar
    else:
        from typing import ParamSpec, TypeVar

    P = ParamSpec("P")
    T = TypeVar("T")

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

RE_CONTRACTION_ENDINGS = r"[tsd]|ve|ll|re"
RE_CONTRACTION_APOSTROPHE = r"\'(?=" + RE_CONTRACTION_ENDINGS + ")"
RE_NONCONTRACTION_APOSTROPHE = r"\'(?!" + RE_CONTRACTION_ENDINGS + ")"

CACHE_SIZE = 128
