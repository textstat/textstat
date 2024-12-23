from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..utils._get_lang_easy_words import get_lang_easy_words
from ..counts._count_syllables import count_syllables


@typed_cache
def is_difficult_word(word: str, syllable_threshold: int, lang: str) -> bool:
    """Return True if `word` is a difficult word.

    The function checks if if the word is in the Dale-Chall list of
    easy words. However, it currently doesn't check if the word is a
    regular inflection of a word in the Dale-Chall list!

    Parameters
    ----------
    word : str
        A word.
    syllable_threshold : int, optional
        Minimum number of syllables a difficult word must have. The
        default is 2.

    Returns
    -------
    bool
        True if the word is not in the easy words list and is longer than
        `syllable_threshold`; else False.

    """
    # Not a word
    if len(word.split()) != 1:
        return False

    easy_word_set = get_lang_easy_words(lang)

    # Not hard
    if word in easy_word_set:
        return False

    # Too short
    if count_syllables(word, lang) < syllable_threshold:
        return False

    return True
