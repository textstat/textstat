from __future__ import annotations

import re

from ..utils._typed_cache import typed_cache
from ..transformations._remove_punctuation import remove_punctuation


@typed_cache
def count_letters(text: str) -> int:
    """Count letters in a text. Spaces are ignored.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        The number of letters in text.

    """
    # Ignore spaces
    text = re.sub(r"\s", "", text)
    return len(remove_punctuation(text, rm_apostrophe=True))
