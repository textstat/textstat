from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..selections._list_words import list_words


@typed_cache
def count_words(text: str, removepunct: bool = True) -> int:
    """Count types (words) in a text.

    English contractions (e.g. "aren't") are counted as one word.
    Hyphenated words are also counted as a single word
    (e.g. "singer-songwriter").

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    count : int
        DESCRIPTION.

    """
    return len(list_words(text, rm_punctuation=removepunct))
