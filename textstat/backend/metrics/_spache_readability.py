from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_words import count_words
from ..counts._count_difficult_words import count_difficult_words
from ._words_per_sentence import words_per_sentence


@typed_cache
def spache_readability(text: str, lang: str) -> float:
    """Calculate SPACHE readability formula for young readers.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The SPACHE readability score for `text`
    """
    total_no_of_words = count_words(text)
    asl = words_per_sentence(text)
    try:
        pdw = 100 * count_difficult_words(text, lang) / total_no_of_words
    except ZeroDivisionError:
        return 0.0
    return (0.141 * asl) + (0.086 * pdw) + 0.839
