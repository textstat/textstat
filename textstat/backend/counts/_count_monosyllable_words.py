from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..transformations._remove_punctuation import remove_punctuation
from ._count_syllables import count_syllables


@typed_cache
def count_monosyllable_words(text: str, lang: str) -> int:
    """counts monosyllable words"""
    word_list = remove_punctuation(text, rm_apostrophe=True).split()
    return len([w for w in word_list if count_syllables(w, lang) < 2])
