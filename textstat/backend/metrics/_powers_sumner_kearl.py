from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._words_per_sentence import words_per_sentence
from ._syllables_per_word import syllables_per_word


@typed_cache
def powers_sumner_kearl(text: str, lang: str) -> float:
    r"""Calculate the Powers-Sumner-Kearl grade level for `text`.

    Powers, Sumner and Kearl (1958) recalculated the Flesch formula for
    texts written for primary school readers (grades 1 to 4).

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The Powers-Sumner-Kearl grade level for `text`.

    Notes
    -----
    The Powers-Sumner-Kearl grade level is calculated as:

    .. math::

        (0.0778*avg\ sentence\ length)+(0.0455*syllables\ per\ 100\ words)-2.2029

    """
    sentence_length = words_per_sentence(text)
    syllables = syllables_per_word(text, lang)

    if sentence_length == 0 or syllables == 0:
        return 0.0

    return (0.0778 * sentence_length) + (0.0455 * 100 * syllables) - 2.2029
