from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_long_words import count_long_words
from ..counts._count_sentences import count_sentences


@typed_cache
def rix(text: str) -> float:
    r"""Calculate the RIX for `text`

    A Rix ratio is the number of long words divided by
    the number of assessed sentences.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The RIX for `text`.

    Notes
    -----
    The estimate of the RIX score is calculated as:

    .. math::

        rix = LW/S

    LW= Number of long words (i.e. words of 7 or more characters)
    S= Number of sentences

    Anderson (1983) specifies that punctuation should be removed and that
    hyphenated sequences and abbreviations count as single words.

    """
    long_words_count = count_long_words(text)
    sentences_count = count_sentences(text)

    try:
        return long_words_count / sentences_count
    except ZeroDivisionError:
        return 0.0
