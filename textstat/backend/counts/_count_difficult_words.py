from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..selections._list_difficult_words import list_difficult_words


@typed_cache
def count_difficult_words(text: str, lang: str, syllable_threshold: int = 2) -> int:
    """Count the number of difficult words.

    Parameters
    ----------
    text : str
        A text string.
    syllable_threshold : int, optional
        The cut-off for the number of syllables difficult words are
        required to have. The default is 2.

    Returns
    -------
    int
        Number of difficult words.

    """
    return len(list_difficult_words(text, syllable_threshold, lang))
