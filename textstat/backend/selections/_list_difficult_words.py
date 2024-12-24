from __future__ import annotations


from ..transformations._remove_punctuation import remove_punctuation
from ..validations._is_difficult_word import is_difficult_word
from ..utils._typed_cache import typed_cache


@typed_cache
def list_difficult_words(text: str, syllable_threshold: int, lang: str) -> list[str]:
    """Get a list of difficult words

    Parameters
    ----------
    text : str
        A text string.
    syllable_threshold : int, optional
        The cut-off for the number of syllables difficult words are
        required to have.

    Returns
    -------
    List[str]
        A list of the words deemed difficult.

    """
    words = remove_punctuation(text.lower(), rm_apostrophe=False).split()
    diff_words = [
        word for word in words if is_difficult_word(word, syllable_threshold, lang)
    ]
    return diff_words
