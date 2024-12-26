from __future__ import annotations


from ..validations._is_difficult_word import is_difficult_word
from ..utils._typed_cache import typed_cache
from ._list_words import list_words


@typed_cache
def list_difficult_words(text: str, syllable_threshold: int, lang: str) -> list[str]:
    """Get a list of the difficult words in the text.

    Parameters
    ----------
    text : str
        A text string.
    syllable_threshold : int, optional
        The cut-off for the number of syllables difficult words are
        required to have.
    lang : str
        The language of the text.

    Returns
    -------
    List[str]
        A list of the words deemed difficult.

    """
    words = list_words(text)
    diff_words = [
        word for word in words if is_difficult_word(word, syllable_threshold, lang)
    ]
    return diff_words
