
from ..utils import typed_cache
from ..counts import count_words, count_sentences, count_difficult_words

@typed_cache
def spache_readability(text: str, lang: str) -> float:
    """
    Function to calculate SPACHE readability formula for young readers.
    I/P - a text
    O/P - an int Spache Readability Index/Grade Level
    """
    total_no_of_words = count_words(text)
    count_of_sentences = count_sentences(text)
    try:
        asl = total_no_of_words / count_of_sentences
        pdw = (count_difficult_words(text, lang) / total_no_of_words) * 100
    except ZeroDivisionError:
        return 0.0
    return (0.141 * asl) + (0.086 * pdw) + 0.839

