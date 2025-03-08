from __future__ import annotations


from ..utils._typed_cache import typed_cache
from ..selections._set_difficult_words import set_difficult_words
from ..selections._list_difficult_words import list_difficult_words


@typed_cache
def count_difficult_words(
    text: str, lang: str, syllable_threshold: int = 2, unique: bool = False
) -> int:
    """Count the number of difficult words. By default, counts all words,
    but can be set to count only unique words by using `unique=True`.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.
    syllable_threshold : int, optional
        The cut-off for the number of syllables difficult words are
        required to have. The default is 2.
    unique : bool, optional
        Count only unique words. The default is False.

    Returns
    -------
    int
        Number of difficult words.

    """
    if unique:
        return len(set_difficult_words(text, syllable_threshold, lang))
    return len(list_difficult_words(text, syllable_threshold, lang))
