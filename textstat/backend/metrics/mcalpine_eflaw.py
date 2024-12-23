
from ..utils import typed_cache
from ..counts import count_words, count_sentences, count_miniwords

@typed_cache
def mcalpine_eflaw(text: str) -> float:
    """
    McAlpine EFLAW score that asseses the readability of English texts
    for English foreign learners

    https://strainindex.wordpress.com/2009/04/30/mcalpine-eflaw-readability-score/
    """

    if len(text) < 1:
        return 0.0

    n_words = count_words(text)
    n_sentences = count_sentences(text)
    n_miniwords = count_miniwords(text, max_size=3)
    return (n_words + n_miniwords) / n_sentences
