from __future__ import annotations

from ..selections._list_words import list_words
from ..utils._get_pyphen import get_pyphen
from ..utils._typed_cache import typed_cache


@typed_cache
def count_syllables(text: str, lang: str) -> int:
    """Estimate the total number of syllables in a text.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    int
        Number of syllables in the text.
    """
    pyphen = get_pyphen(lang)

    return sum([len(pyphen.positions(w)) + 1 for w in list_words(text, lowercase=True)])
