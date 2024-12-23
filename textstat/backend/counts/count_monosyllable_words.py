
from ..utils import typed_cache
from ..transformations import remove_punctuation
from . import count_syllables

@typed_cache
def count_monosyllable_words(text: str, lang: str) -> int:
    """counts monosyllables"""
    word_list = remove_punctuation(text, rm_apostrophe=True).split()
    return len([w for w in word_list if count_syllables(w, lang) < 2])
