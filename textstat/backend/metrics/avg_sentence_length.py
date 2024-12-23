
from ..utils import typed_cache
from ..counts import count_words, count_sentences

@typed_cache
def avg_sentence_length(text: str) -> float:
    """Calculate the average sentence length.

    This function is a combination of the functions `counts.lexicon_count` and
    `counts.sentence_count`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The average sentence length.

    """
    try:
        return count_words(text) / count_sentences(text)
    except ZeroDivisionError:
        return 0.0
