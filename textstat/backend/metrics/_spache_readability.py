from ..utils._typed_cache import typed_cache
from ..counts._count_words import count_words
from ..counts._count_difficult_words import count_difficult_words
from ._words_per_sentence import words_per_sentence


@typed_cache
def spache_readability(text: str, lang: str) -> float:
    """
    Function to calculate SPACHE readability formula for young readers.
    I/P - a text
    O/P - an int Spache Readability Index/Grade Level
    """
    total_no_of_words = count_words(text)
    try:
        asl = words_per_sentence(text)
        pdw = (count_difficult_words(text, lang) / total_no_of_words) * 100
    except ZeroDivisionError:
        return 0.0
    return (0.141 * asl) + (0.086 * pdw) + 0.839
