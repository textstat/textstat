from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..utils._get_lang_root import get_lang_root
from ..utils._get_lang_cfg import get_lang_cfg
from ._syllables_per_word import syllables_per_word
from ._words_per_sentence import words_per_sentence


@typed_cache
def flesch_reading_ease(text: str, lang: str) -> float:
    """Calculate the Flesch Reading Ease formula.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The Flesch Reading Ease for `text`.
    """
    lang_root = get_lang_root(lang)
    sentence_length = words_per_sentence(text)
    syllables = syllables_per_word(text, lang)

    if sentence_length == 0 or syllables == 0:
        return 0.0

    return (
        get_lang_cfg(lang_root, "fre_base")
        - get_lang_cfg(lang_root, "fre_sentence_length") * sentence_length
        - get_lang_cfg(lang_root, "fre_syll_per_word") * syllables
    )
