from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_words import count_words
from ..counts._count_polysyllable_words import count_polysyllable_words
from ..counts._count_long_words import count_long_words
from ..counts._count_monosyllable_words import count_monosyllable_words
from ._words_per_sentence import words_per_sentence


@typed_cache
def wiener_sachtextformel(text: str, variant: int, lang: str) -> float:
    """Calculate Wiener Sachtextformel for readability assessment of German texts

    https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel

    Parameters
    ----------
    text : str
        A text string.
    variant : int
        The variant of the formula.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The Wiener Sachtextformel readability score for `text`
    """
    n_words = count_words(text)

    try:
        ms = 100 * count_polysyllable_words(text, lang) / n_words
        sl = words_per_sentence(text)
        iw = 100 * count_long_words(text) / n_words
        es = 100 * count_monosyllable_words(text, lang) / n_words
    except ZeroDivisionError:
        return 0.0

    if variant == 1:
        return (0.1935 * ms) + (0.1672 * sl) + (0.1297 * iw) - (0.0327 * es) - 0.875
    elif variant == 2:
        return (0.2007 * ms) + (0.1682 * sl) + (0.1373 * iw) - 2.779
    elif variant == 3:
        return (0.2963 * ms) + (0.1905 * sl) - 1.1144
    elif variant == 4:
        return (0.2744 * ms) + (0.2656 * sl) - 1.693
    else:
        raise ValueError("variant can only be an integer between 1 and 4")
