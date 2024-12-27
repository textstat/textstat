from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_words import count_words
from ..counts._count_difficult_words import count_difficult_words
from ._words_per_sentence import words_per_sentence


@typed_cache
def dale_chall_readability_score_v2(text: str, lang: str) -> float:
    """Calculate New Dale Chall Readability formula.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The New Dale Chall Readability Score for `text`
    """
    total_no_of_words = count_words(text)
    try:
        asl = words_per_sentence(text)
        pdw = 100 * count_difficult_words(text, lang) / total_no_of_words
    except ZeroDivisionError:
        return 0.0
    raw_score = 0.1579 * (pdw) + 0.0496 * asl
    adjusted_score = raw_score
    if raw_score > 0.05:
        adjusted_score = raw_score + 3.6365
    return adjusted_score
