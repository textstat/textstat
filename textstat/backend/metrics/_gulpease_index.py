from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._sentences_per_word import sentences_per_word
from ._chars_per_word import chars_per_word


@typed_cache
def gulpease_index(text: str) -> float:
    """Calculate Indice Gulpease Index for Italian texts
    https://it.wikipedia.org/wiki/Indice_Gulpease

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The Gulpease Index for `text`
    """
    spw = sentences_per_word(text)
    cpw = chars_per_word(text)

    if spw == 0 or cpw == 0:
        return 0.0

    return (300 * spw) - (10 * cpw) + 89
