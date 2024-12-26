from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_words import count_words
from ..counts._count_difficult_words import count_difficult_words
from ._words_per_sentence import words_per_sentence


@typed_cache
def dale_chall_readability_score(text: str, lang: str) -> float:
    r"""Estimate the Dale-Chall readability score.

    Deviations from the original Dale-Chall readability score:
    - For now, regular inflections of words in the Dale-Chall list of easy
        words are counted as difficult words
        (see documentation for `is_difficult_word`). This may change in the
        future.
    - Proper names are also counted as difficult words. This is unlikely to
        change.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        An approximation of the Dale-Chall readability score.

    Notes
    -----
    The estimate of the Dale-Chall readability score is calculated as:

    .. math::

        (0.1579*%\ difficult\ words)+(0.0496*avg\ words\ per\ sentence)

    If the percentage of difficult words is > 5, 3.6365 is added to the
    score.
    """
    word_count = count_words(text)
    hard_count = count_difficult_words(text, lang, syllable_threshold=0)

    try:
        per_difficult_words = 100 * hard_count / word_count
    except ZeroDivisionError:
        return 0.0

    score = (0.1579 * per_difficult_words) + (0.0496 * words_per_sentence(text))

    if per_difficult_words > 5:
        score += 3.6365
    return score
