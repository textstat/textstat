
from ..utils import typed_cache
from ..counts import count_letters, count_words

@typed_cache
def letters_per_word(text: str) -> float:
    """Calculate the average sentence word length in letters.

    This function is a combination of the functions `counts.letter_count` and
    `counts.lexicon_count`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The average number of letters per word.

    """
    try:
        return count_letters(text) / count_words(text)
    except ZeroDivisionError:
        return count_letters(text)
