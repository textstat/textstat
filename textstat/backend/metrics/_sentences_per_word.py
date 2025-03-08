from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_sentences import count_sentences
from ..counts._count_words import count_words


@typed_cache
def sentences_per_word(text: str) -> float:
    """Get the number of sentences per word.

    A combination of the functions counts.count_sentences and counts.count_words.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        Number of sentences per word.

    """
    try:
        return count_sentences(text) / count_words(text)
    except ZeroDivisionError:
        return 0.0
