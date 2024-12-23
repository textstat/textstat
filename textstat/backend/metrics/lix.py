from ..utils import typed_cache
from ..counts import count_long_words, count_words
from . import avg_sentence_length

@typed_cache
def lix(text: str) -> float:
    r"""Calculate the LIX for `text`

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    TYPE
        DESCRIPTION.

    Notes
    -----
    The estimate of the LIX score is calculated as:

    .. math::

        LIX = A/B + A*100/C

    A= Number of words
    B= Number of sentences
    C= Number of long words (More than 6 letters)

    `A` is obtained with `len(text.split())`, which counts
    contractions as one word. `A/B` is
    calculated using the method `textstat.avg_sentence_length()`, which
    counts contractions as two words, unless `__rm_apostrophe` is set to
    False. Therefore, the definition of a word is only consistent if you
    call `textstat.set_rm_apostrophe(False)` before calculating the LIX.

    """
    words_len = count_words(text)
    long_words = count_long_words(text)
    try:
        per_long_words = (long_words * 100) / words_len
    except ZeroDivisionError:
        return 0.0
    asl = avg_sentence_length(text)
    return asl + per_long_words
