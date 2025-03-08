from __future__ import annotations


from ..utils._typed_cache import typed_cache
from ..utils._get_lang_cfg import get_lang_cfg
from ..counts._count_words import count_words
from ..counts._count_difficult_words import count_difficult_words
from ._words_per_sentence import words_per_sentence


@typed_cache
def gunning_fog(text: str, lang: str) -> float:
    """Calculate the Gunning Fog Index formula.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The Gunning Fog Index for `text`.
    """
    syllable_threshold = int(get_lang_cfg(lang, "syllable_threshold"))
    diff_words = count_difficult_words(text, lang, syllable_threshold)
    tot_words = count_words(text)

    try:
        per_diff_words = 100 * diff_words / tot_words
    except ZeroDivisionError:
        return 0.0

    return 0.4 * (words_per_sentence(text) + per_diff_words)
