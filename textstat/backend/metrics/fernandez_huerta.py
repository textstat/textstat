
from ..utils import typed_cache
from . import avg_sentence_length, syllables_per_word

@typed_cache
def fernandez_huerta(text: str, lang: str) -> float:
    """
    Fernandez Huerta readability score
    https://legible.es/blog/lecturabilidad-fernandez-huerta/
    """
    sentence_length = avg_sentence_length(text)
    syllables = syllables_per_word(text, lang)

    return 206.84 - float(60 * syllables) - float(1.02 * sentence_length)