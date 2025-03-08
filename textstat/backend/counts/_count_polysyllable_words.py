from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._count_syllables import count_syllables
from ..selections._list_words import list_words


@typed_cache
def count_polysyllable_words(text: str, lang: str) -> int:
    """Count the words with three or more syllables. Contractions and hyphenations
    are counted as one word.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    int
        Number of words with three or more syllables.

    """
    return len([w for w in list_words(text) if count_syllables(w, lang) >= 3])
