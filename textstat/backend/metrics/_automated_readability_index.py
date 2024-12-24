from __future__ import annotations

from ._words_per_sentence import words_per_sentence
from ._chars_per_word import chars_per_word

from ..utils._typed_cache import typed_cache


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
    a = chars_per_word(text)
    b = words_per_sentence(text)

    if a == 0 or b == 0:
        return 0.0

    return (4.71 * a) + (0.5 * b) - 21.43
