
from ..utils import typed_cache
from ..counts import count_words, count_difficult_words
from . import words_per_sentence

@typed_cache
def dale_chall_readability_score_v2(text: str, lang: str) -> float:
    """
    Function to calculate New Dale Chall Readability formula.
    I/P - a text
    O/P - an int Dale Chall Readability Index/Grade Level
    """
    total_no_of_words = count_words(text)
    try:
        asl = words_per_sentence(text)
        pdw = (count_difficult_words(text, lang) / total_no_of_words) * 100
    except ZeroDivisionError:
        return 0.0
    raw_score = 0.1579 * (pdw) + 0.0496 * asl
    adjusted_score = raw_score
    if raw_score > 0.05:
        adjusted_score = raw_score + 3.6365
    return adjusted_score
