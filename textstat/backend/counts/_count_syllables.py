from __future__ import annotations

from ..transformations._remove_punctuation import remove_punctuation
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
    text = text.lower()
    text = remove_punctuation(text, rm_apostrophe=False)

    if not text:
        return 0

    pyphen = get_pyphen(lang)

    return sum([len(pyphen.positions(w)) + 1 for w in text.split()])
