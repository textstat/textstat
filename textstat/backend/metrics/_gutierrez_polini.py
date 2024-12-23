from ..utils._typed_cache import typed_cache
from ..counts._count_words import count_words
from ..counts._count_letters import count_letters
from ..counts._count_sentences import count_sentences


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
