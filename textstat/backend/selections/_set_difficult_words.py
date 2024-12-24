from __future__ import annotations


from ..utils._typed_cache import typed_cache
from ._list_difficult_words import list_difficult_words


@typed_cache
def set_difficult_words(text: str, syllable_threshold: int, lang: str) -> set[str]:
    """Get a set of difficult words

    Parameters
    ----------
    text : str
        A text string.
    syllable_threshold : int, optional
        The cut-off for the number of syllables difficult words are
        required to have.

    Returns
    -------
    set[str]
        A set of the words deemed difficult.

    """
    return set(list_difficult_words(text, syllable_threshold, lang))
