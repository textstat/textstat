from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_words import count_words
from ..counts._count_sentences import count_sentences


@typed_cache
def words_per_sentence(text: str) -> float:
    """Calculate the average number of words per sentence.

    This function is a combination of the functions `counts.count_words` and
    `counts.count_sentences`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The average number of words per sentence.

    """
    try:
        return count_words(text) / count_sentences(text)
    except ZeroDivisionError:
        return 0.0
