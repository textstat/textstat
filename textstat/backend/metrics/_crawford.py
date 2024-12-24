from __future__ import annotations


from ..utils._typed_cache import typed_cache
from ._sentences_per_word import sentences_per_word
from ._syllables_per_word import syllables_per_word


@typed_cache
def crawford(text: str, lang: str) -> float:
    """
    Crawford index
    https://legible.es/blog/formula-de-crawford/
    """
    # Calculating __ per 100 words
    sentences_per_words = 100 * sentences_per_word(text)
    syllables_per_words = 100 * syllables_per_word(text, lang)

    if sentences_per_words == 0 or syllables_per_words == 0:
        return 0.0

    return -0.205 * sentences_per_words + 0.049 * syllables_per_words - 3.407
