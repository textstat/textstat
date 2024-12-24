from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_syllables import count_syllables
from ..counts._count_sentences import count_sentences
from ..selections._list_words import list_words


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
    # TODO: this implementation is slightly off, but only for weird text
    # Specifically, the "first 100 words" as implemented will count " . "
    # as its own word. I don't know how to fix this yet but it should be
    # done at some point. Also, args for enforcing the upper and lower bounds
    # on the 100 word count should be added so that users aren't locked into
    # a loose lower bound but tight upper bound.
    easy_word = 0
    difficult_word = 0
    text_list = list_words(text, rm_punctuation=False)[:100]

    for word in text_list:
        n_syll = count_syllables(word, lang)
        if n_syll >= 3:
            difficult_word += 1
        elif n_syll > 0:
            easy_word += 1

    text = " ".join(text_list)

    try:
        number = float((easy_word * 1 + difficult_word * 3) / count_sentences(text))
    except ZeroDivisionError:
        return 0.0

    if number <= 20:
        number -= 2

    return number / 2
