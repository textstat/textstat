from ..utils._typed_cache import typed_cache
from ._sentences_per_word import sentences_per_word
from ._chars_per_word import chars_per_word


@typed_cache
def gulpease_index(text: str) -> float:
    """
    Indice Gulpease Index for Italian texts
    https://it.wikipedia.org/wiki/Indice_Gulpease
    """

    if len(text) == 0:
        return 0.0

    return (300 * sentences_per_word(text)) - (10 * chars_per_word(text)) + 89
