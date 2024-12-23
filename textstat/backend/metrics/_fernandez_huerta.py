from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._words_per_sentence import words_per_sentence
from ._syllables_per_word import syllables_per_word


@typed_cache
def fernandez_huerta(text: str, lang: str) -> float:
    """
    Fernandez Huerta readability score
    https://legible.es/blog/lecturabilidad-fernandez-huerta/
    """
    sentence_length = words_per_sentence(text)
    syllables = syllables_per_word(text, lang)

    return 206.84 - float(60 * syllables) - float(1.02 * sentence_length)
