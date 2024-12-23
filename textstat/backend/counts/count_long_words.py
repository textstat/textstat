
from ..utils import typed_cache
from ..transformations import remove_punctuation


@typed_cache
def count_long_words(text: str) -> int:
    """counts words with more than 6 characters"""
    word_list = remove_punctuation(text, rm_apostrophe=True).split()
    return len([w for w in word_list if len(w) > 6])
