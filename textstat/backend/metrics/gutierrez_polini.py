
from ..utils import typed_cache
from ..counts import count_words, count_letters, count_sentences

@typed_cache
def gutierrez_polini(text: str) -> float:
    """
    Guttierrez de Polini index
    https://legible.es/blog/comprensibilidad-gutierrez-de-polini/
    """
    total_words = count_words(text)
    total_letters = count_letters(text)
    total_sentences = count_sentences(text)

    try:
        return (
            95.2
            - 9.7 * (total_letters / total_words)
            - 0.35 * (total_words / total_sentences)
        )
    except ZeroDivisionError:
        return 0.0
