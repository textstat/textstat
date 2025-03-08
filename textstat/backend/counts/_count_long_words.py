from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..selections._list_words import list_words


@typed_cache
def count_long_words(text: str, threshold: int = 6) -> int:
    """Counts words with more than `threshold` letters.

    Parameters
    ----------
    text : str
        A text string.
    threshold : int, optional
        The cut-off for the number of letters. The default is 6.

    Returns
    -------
    int
        Number of words with more than `threshold` letters.
    """
    return len([w for w in list_words(text, rm_apostrophe=True) if len(w) > threshold])
