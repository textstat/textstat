
from ..utils import typed_cache
from ..counts import count_words, count_sentences

@typed_cache
def words_per_sentence(text: str) -> float:
    """Calculate the average number of words per sentence.

    This function is a combination of the functions `counts.lexicon_count` and
    `counts.sentence_count`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The average number of words per sentence.

    """
    try:
        return count_words(text) / count_sentences(text)
    except ZeroDivisionError:
        return count_words(text)
