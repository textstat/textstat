from __future__ import annotations


from ..utils._typed_cache import typed_cache
from ._letters_per_word import letters_per_word
from ._words_per_sentence import words_per_sentence


@typed_cache
def gutierrez_polini(text: str) -> float:
    """
    Guttierrez de Polini index
    https://legible.es/blog/comprensibilidad-gutierrez-de-polini/
    """
    lpw = letters_per_word(text)
    wps = words_per_sentence(text)

    if lpw == 0 or wps == 0:
        return 0.0

    return 95.2 - 9.7 * lpw - 0.35 * wps
