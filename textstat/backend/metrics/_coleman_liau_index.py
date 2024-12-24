from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ._letters_per_word import letters_per_word
from ._sentences_per_word import sentences_per_word


@typed_cache
def coleman_liau_index(text: str) -> float:
    r"""Calculate the Coleman-Liaux index.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The Coleman-Liaux index for `text`.

    Notes
    -----
    The Coleman-Liaux index is calculated as:

    .. math::

        (0.058*n\ letters/n\ words)-(0.296*n\ sentences/n\ words)-15.8

    """
    letters = letters_per_word(text) * 100
    sentences = sentences_per_word(text) * 100

    if letters == 0 or sentences == 0:
        return 0.0

    return (0.058 * letters) - (0.296 * sentences) - 15.8
