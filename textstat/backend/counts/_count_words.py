from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..selections._list_words import list_words


@typed_cache
def count_words(
    text: str,
    rm_punctuation: bool = True,
    split_contractions: bool = False,
    split_hyphens: bool = False,
) -> int:
    """Count the number of words in a text.

    By default, English contractions (e.g. "aren't") and hyphenated words are counted
    as one word. If `split_contractions` is set to True, contractions are counted as
    multiple words. If `split_hyphens` is set to True, hyphenated words are counted
    as multiple words. If `rm_punctuation` is set to False, "words" with no letters
    (e.g. " .? ") are counted as words.

    Parameters
    ----------
    text : str
        A text string.
    rm_punctuation : bool, optional
        Remove punctuation. The default is True.
    split_contractions : bool, optional
        Split contractions. The default is False.
    split_hyphens : bool, optional
        Split hyphenated words. The default is False.

    Returns
    -------
    count : int
        Number of words.

    """
    return len(
        list_words(
            text,
            rm_punctuation=rm_punctuation,
            split_contractions=split_contractions,
            split_hyphens=split_hyphens,
        )
    )
