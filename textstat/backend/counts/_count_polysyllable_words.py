from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._count_syllables import count_syllables
from ..selections._list_words import list_words


@typed_cache
def count_polysyllable_words(text: str, lang: str) -> int:
    """Count the words with three or more syllables.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of words with three or more syllables.

    Notes
    -----
    The function uses text.split() to generate a list of words.
    Contractions and hyphenations are therefore counted as one word.

    """
    return len([w for w in list_words(text) if count_syllables(w, lang) >= 3])
