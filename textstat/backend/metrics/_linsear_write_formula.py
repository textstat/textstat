from ..utils._typed_cache import typed_cache
from ..counts._count_syllables import count_syllables
from ..counts._count_sentences import count_sentences


@typed_cache
def linsear_write_formula(text: str, lang: str) -> float:
    r"""Calculate the Linsear-Write (Lw) metric.

    The Lw only uses the first 100 words of text!

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The Lw for `text`.

    Notes
    -----
    The Lw is calculated using the first 100 words:

    .. math::

        n\ easy\ words+(n\ difficult\ words*3))/n\ sentences

    easy words are defined as words with 2 syllables or less.
    difficult words are defined as words with 3 syllables or more.
    r"""
    easy_word = 0
    difficult_word = 0
    text_list = text.split()[:100]

    for word in text_list:
        if count_syllables(word, lang) < 3:
            easy_word += 1
        else:
            difficult_word += 1

    text = " ".join(text_list)

    try:
        number = float((easy_word * 1 + difficult_word * 3) / count_sentences(text))
    except ZeroDivisionError:
        return 0.0

    if number <= 20:
        number -= 2

    return number / 2
