from __future__ import annotations

import re

from ..utils._typed_cache import typed_cache
from ..selections._list_words import list_words


@typed_cache
def count_arabic_syllables(text: str, rm_apostrophe: bool = True) -> int:
    """Count arabic syllables.

    Long and stressed syllables are counted double.

    Parameters
    ----------
    text : str
        A text string.
    rm_apostrophe : bool, optional
        Remove apostrophes with other punctuation. The default is True.

    Returns
    -------
    int
        Number of arabic syllables.

    """
    short_count = 0
    long_count = 0

    # tashkeel: fatha | damma | kasra
    tashkeel = [r"\u064E", r"\u064F", r"\u0650"]
    char_list = [c for w in list_words(text, rm_apostrophe=rm_apostrophe) for c in w]

    for t in tashkeel:
        for i, c in enumerate(char_list):
            if c != t:
                continue

            # only if a character is a tashkeel, has a successor
            # and is followed by an alef, waw or yaaA ...
            if i + 1 < len(char_list) and char_list[i + 1] in [
                "\u0627",
                "\u0648",
                "\u064a",
            ]:
                # ... increment long syllable count
                long_count += 1
            else:
                short_count += 1

    # stress syllables: tanween fatih | tanween damm | tanween kasr
    # | shadda
    stress_pattern = re.compile(r"[\u064B\u064C\u064D\u0651]")
    stress_count = len(stress_pattern.findall(text))

    if short_count == 0:
        text = re.sub(r"[\u0627\u0649\?\.\!\,\s*]", "", text)
        short_count = len(text) - 2

    return short_count + 2 * (long_count + stress_count)
