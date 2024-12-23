
from ..utils import typed_cache
from . import avg_sentence_length, syllables_per_word

@typed_cache
def flesch_kincaid_grade(text: str, lang: str) -> float:
    r"""Calculate the Flesh-Kincaid Grade for `text`.

    Parameters
    ----------
    text : str
        A text string.

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
    sentence_length = avg_sentence_length(text)
    syllables = syllables_per_word(text, lang)
    return (0.39 * sentence_length) + (11.8 * syllables) - 15.59
