from __future__ import annotations

import re


from ..utils._typed_cache import typed_cache
from ..selections._list_words import list_words


@typed_cache
def count_arabic_long_words(text: str, rm_apostrophe: bool = True) -> int:
    """Counts long arabic words (>5 letters) without short vowels (tashkeel).


    Parameters
    ----------
    text : str
        A text string.
    rm_apostrophe : bool, optional
        Remove apostrophes with other punctuation. The default is True.

    Returns
    -------
    int
        Number of long arabic words without short vowels (tashkeel).

    """
    tashkeel = (
        r"\u064E|\u064B|\u064F|\u064C|\u0650|\u064D|\u0651|"
        + r"\u0652|\u0653|\u0657|\u0658"
    )
    # remove tashkeel
    text = re.sub(tashkeel, "", text)

    count = 0
    for t in list_words(text, rm_apostrophe=rm_apostrophe):
        if len(t) > 5:
            count += 1

    return count
