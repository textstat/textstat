
from ..utils import typed_cache
from ..counts import count_sentences, count_words

@typed_cache
def sentences_per_word(text: str) -> float:
    """Get the number of sentences per word.

    A combination of the functions counts.sentence_count and lecicon_count.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        Number of sentences per word.

    """
    try:
        return count_sentences(text) / count_words(text)
    except ZeroDivisionError:
        return 0.0
