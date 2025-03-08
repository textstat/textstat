from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._words_per_sentence import words_per_sentence
from ._syllables_per_word import syllables_per_word


@typed_cache
def flesch_kincaid_grade(text: str, lang: str) -> float:
    r"""Calculate the Flesh-Kincaid Grade for `text`.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The Flesh-Kincaid Grade for `text`.

    Notes
    -----
    The Flesh-Kincaid Grade is calculated as:

    .. math::

        (.39*avg\ sentence\ length)+(11.8*avg\ syllables\ per\ word)-15.59

    """
    sentence_length = words_per_sentence(text)
    syllables = syllables_per_word(text, lang)

    if sentence_length == 0 or syllables == 0:
        return 0.0

    return (0.39 * sentence_length) + (11.8 * syllables) - 15.59
