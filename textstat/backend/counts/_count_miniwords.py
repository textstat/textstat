from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..selections._list_words import list_words


@typed_cache
def count_miniwords(text: str, max_size: int = 3) -> int:
    """Count common words with `max_size` letters or less in a text.

    Parameters
    ----------
    text : str
        A text string.
    max_size : int, optional
        Maximum number of letters in a word for it to be counted.

    Returns
    -------
    count : int

    """
    count = len(
        [word for word in list_words(text, rm_apostrophe=True) if len(word) <= max_size]
    )
    return count
