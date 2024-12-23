
from ..utils import typed_cache
from ..counts import count_sentences, count_words, count_syllables

@typed_cache
def crawford(text: str, lang: str) -> float:
    """
    Crawford index
    https://legible.es/blog/formula-de-crawford/
    """
    total_sentences = count_sentences(text)
    total_words = count_words(text)
    total_syllables = count_syllables(text, lang)

    # Calculating __ per 100 words
    try:
        sentences_per_words = 100 * (total_sentences / total_words)
        syllables_per_words = 100 * (total_syllables / total_words)
    except ZeroDivisionError:
        return 0.0

    return -0.205 * sentences_per_words + 0.049 * syllables_per_words - 3.407
