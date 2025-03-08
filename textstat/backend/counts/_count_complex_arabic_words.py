from __future__ import annotations

import re

from ..utils._typed_cache import typed_cache
from ..selections._list_words import list_words


@typed_cache
def count_complex_arabic_words(text: str, rm_apostrophe: bool = True) -> int:
    """
    Count complex arabic words. Complex arabic words are word with
    more than 5 instances between the following:
    - fatha
    - tanween fath
    - dhamma
    - tanween dhamm
    - kasra
    - tanween kasr
    - shaddah

    Parameters
    ----------
    text : str
        A text string.
    rm_apostrophe : bool, optional
        Remove apostrophes with other punctuation. The default is True.

    Returns
    -------
    int
        Number of arabic complex words.

    """
    count = 0

    # fatHa | tanween fatH | dhamma | tanween dhamm
    # | kasra | tanween kasr | shaddah
    pattern = re.compile("[\u064e\u064b\u064f\u064c\u0650\u064d\u0651]")

    for w in list_words(text, rm_apostrophe=rm_apostrophe):
        if len(pattern.findall(w)) > 5:
            count += 1

    return count
