from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_long_words import count_long_words
from ..counts._count_words import count_words
from ._words_per_sentence import words_per_sentence


@typed_cache
def lix(text: str) -> float:
    r"""Calculate the LIX for `text`

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The LIX score for `text`.

    Notes
    -----
    The estimate of the LIX score is calculated as:

    .. math::

        LIX = A/B + A*100/C

    A= Number of words
    B= Number of sentences
    C= Number of long words (More than 6 letters)

    """
    words_len = count_words(text)
    long_words = count_long_words(text)
    try:
        per_long_words = 100 * long_words / words_len
    except ZeroDivisionError:
        return 0.0
    asl = words_per_sentence(text)
    return asl + per_long_words
