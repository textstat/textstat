from __future__ import annotations

import re

from . import validations
from . import utils


@utils.typed_cache
def difficult_words_list(text: str, syllable_threshold: int, lang: str) -> list[str]:
    """Get a list of difficult words

    Parameters
    ----------
    text : str
        A text string.
    syllable_threshold : int, optional
        The cut-off for the number of syllables difficult words are
        required to have. The default is 2.

    Returns
    -------
    List[str]
        A list of the words deemed difficult.

    """
    words = set(re.findall(r"[\w\='‘’]+", text.lower()))
    diff_words = [
        word
        for word in words
        if validations.is_difficult_word(word, syllable_threshold, lang)
    ]
    return diff_words
