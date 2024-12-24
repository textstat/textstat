from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._count_syllables import count_syllables


@typed_cache
def count_monosyllable_words(text: str, lang: str) -> int:
    """counts monosyllable words"""
    return len([w for w in text.split() if count_syllables(w, lang) == 1])
