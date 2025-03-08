from __future__ import annotations

import re

from ..utils._typed_cache import typed_cache
from ._count_words import count_words


@typed_cache
def count_sentences(text: str) -> int:
    """Count the sentences of the text.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of sentences in the text. Will be 0 for empty string, otherwise >= 1.

    """
    if len(text) == 0:
        return 0

    ignore_count = 0
    sentences = re.findall(r"\b[^.!?]+[.!?]*", text, re.UNICODE)
    for sentence in sentences:
        if count_words(sentence) <= 2:
            ignore_count += 1
    return max(1, len(sentences) - ignore_count)
