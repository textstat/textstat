from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_syllables import count_syllables
from ..counts._count_words import count_words


@typed_cache
def syllables_per_word(text: str, lang: str) -> float:
    """Get the average number of syllables per word.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The average number of syllables per word.

    """
    try:
        return count_syllables(text, lang) / count_words(text)
    except ZeroDivisionError:
        return 0.0
