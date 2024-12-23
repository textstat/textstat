
from ..utils import typed_cache
from . import sentences_per_word, chars_per_word

@typed_cache
def gulpease_index(text: str) -> float:
    """
    Indice Gulpease Index for Italian texts
    https://it.wikipedia.org/wiki/Indice_Gulpease
    """

    if len(text) < 1:
        return 0.0

    return (
        (300 * sentences_per_word(text)) - (10 * chars_per_word(text)) + 89
    )
