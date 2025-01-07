from __future__ import annotations


from ..utils._typed_cache import typed_cache
from ._sentences_per_word import sentences_per_word
from ._syllables_per_word import syllables_per_word


@typed_cache
def crawford(text: str, lang: str) -> float:
    r"""Calculate the Crawford index for the text.

    https://legible.es/blog/formula-de-crawford/

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The Crawford index for `text`.

    Notes
    -----
    The Crawford index is calculated as:

    .. math::

        (-0.205*n\ sentences/n\ words)+(0.049*n\ syllables/n\ words)-3.407

    """
    # Calculating __ per 100 words
    sentences_per_words = 100 * sentences_per_word(text)
    syllables_per_words = 100 * syllables_per_word(text, lang)

    if sentences_per_words == 0 or syllables_per_words == 0:
        return 0.0

    return -0.205 * sentences_per_words + 0.049 * syllables_per_words - 3.407
