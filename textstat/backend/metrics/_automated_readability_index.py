from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_chars import count_chars
from ..counts._count_words import count_words
from ..counts._count_sentences import count_sentences


@typed_cache
def automated_readability_index(text: str) -> float:
    r"""Calculate the Automated Readability Index (ARI).

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The ARI for `text`.

    Notes
    -----
    The ARI is calculated as:

    .. math::

        (4.71*n\ characters/n\ words)+(0.5*n\ words/n\ sentences)-21.43

    """
    chrs = count_chars(text, True)
    words = count_words(text)
    sentences = count_sentences(text)
    try:
        a = chrs / words
        b = words / sentences
        return (4.71 * a) + (0.5 * b) - 21.43
    except ZeroDivisionError:
        return 0.0
