from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._letters_per_word import letters_per_word
from ._sentences_per_word import sentences_per_word


@typed_cache
def coleman_liau_index(text: str) -> float:
    r"""Calculate the Coleman-Liau index.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The Coleman-Liau index for `text`.

    Notes
    -----
    The Coleman-Liau index is calculated as:

    .. math::

        (0.0588*L)-(0.296*S)-15.8

    where :math:`L` is the average number of letters per 100 words and
    :math:`S` is the average number of sentences per 100 words.

    """
    letters = letters_per_word(text) * 100
    sentences = sentences_per_word(text) * 100

    if letters == 0 or sentences == 0:
        return 0.0

    return (0.0588 * letters) - (0.296 * sentences) - 15.8
