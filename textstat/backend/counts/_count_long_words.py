from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..selections._list_words import list_words


@typed_cache
def count_long_words(text: str) -> int:
    """counts words with more than 6 letters"""
    return len([w for w in list_words(text, rm_apostrophe=True) if len(w) > 6])
