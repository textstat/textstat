from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._words_per_sentence import words_per_sentence
from ._syllables_per_word import syllables_per_word


@typed_cache
def fernandez_huerta(text: str, lang: str) -> float:
    """Calculate Fernandez Huerta readability score
    https://legible.es/blog/lecturabilidad-fernandez-huerta/

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The Fernandez Huerta readability score for `text`
    """
    sentence_length = words_per_sentence(text)
    syllables = syllables_per_word(text, lang)

    if sentence_length == 0 or syllables == 0:
        return 0.0

    return 206.84 - (60 * syllables) - (1.02 * sentence_length)
