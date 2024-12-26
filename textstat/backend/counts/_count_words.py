from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..selections._list_words import list_words


@typed_cache
def count_words(text: str, rm_punctuation: bool = True) -> int:
    """Count the number of words in a text.

    English contractions (e.g. "aren't") and hyphenated words are counted as one word.
    If `rm_punctuation` is set to False, "words" with no letters (e.g. " .? ") are
    counted as words.

    Parameters
    ----------
    text : str
        A text string.
    rm_punctuation : bool, optional
        Remove punctuation. The default is True.

    Returns
    -------
    count : int
        Number of words.

    """
    return len(list_words(text, rm_punctuation=rm_punctuation))
