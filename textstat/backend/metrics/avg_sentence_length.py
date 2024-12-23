
from . import words_per_sentence

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
    # TODO: deprecation warning
    return words_per_sentence(text)
