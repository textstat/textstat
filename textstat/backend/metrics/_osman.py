from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_words import count_words
from ..counts._count_complex_arabic_words import count_complex_arabic_words
from ..counts._count_arabic_long_words import count_arabic_long_words
from ..counts._count_arabic_syllables import count_arabic_syllables
from ..counts._count_faseeh import count_faseeh
from ._words_per_sentence import words_per_sentence


@typed_cache
def osman(text: str) -> float:
    """Calculate Osman index for Arabic texts
    https://www.aclweb.org/anthology/L16-1038.pdf

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The Osman index for `text`
    """
    try:
        complex_word_rate = count_complex_arabic_words(text) / count_words(text)
        long_word_rate = count_arabic_long_words(text) / count_words(text)
        syllables_per_word = count_arabic_syllables(text) / count_words(text)
        faseeh_per_word = count_faseeh(text) / count_words(text)
    except ZeroDivisionError:
        return 0.0

    return (
        200.791
        - (1.015 * words_per_sentence(text))
        - (
            24.181
            * (
                complex_word_rate
                + syllables_per_word
                + faseeh_per_word
                + long_word_rate
            )
        )
    )
