from __future__ import annotations


from ..utils._typed_cache import typed_cache
from ..counts._count_syllables import count_syllables
from ..counts._count_sentences import count_sentences
from ..selections._list_words import list_words
from ..transformations._remove_punctuation import remove_punctuation


@typed_cache
def linsear_write_formula(
    text: str, lang: str, strict_lower: bool, strict_upper: bool
) -> float:
    r"""Calculate the Linsear-Write (Lw) metric.

    Canonically the Lw only uses the first 100 words of text. To enable this
    functionality, set `strict_upper` to True.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.
    strict_lower : bool
        If True, the Lw is only calculated if the number of words is at least 100.
    strict_upper : bool
        If True, the Lw is only calculated on the first 100 words.

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
    text_list = list_words(text, rm_punctuation=False)

    words_list = []
    i_text = 0
    if strict_upper and len(text_list) > 100:
        while (i_text < len(text_list)) and (len(words_list) < 100):
            word = remove_punctuation(text_list[i_text], rm_apostrophe=False)
            i_text += 1
            if len(word) > 0:
                words_list.append(word)
    else:
        words_list = list_words(text, rm_punctuation=True)
        i_text = len(text_list)

    if strict_lower and len(words_list) < 100:
        return 0.0

    easy_word = 0
    difficult_word = 0
    for word in words_list:
        n_syll = count_syllables(word, lang)
        if n_syll >= 3:
            difficult_word += 1
        elif n_syll > 0:
            easy_word += 1

    text = " ".join(text_list[:i_text])

    try:
        number = float((easy_word * 1 + difficult_word * 3) / count_sentences(text))
    except ZeroDivisionError:
        return 0.0

    if number <= 20:
        number -= 2

    return number / 2
