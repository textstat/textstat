
from ..utils import typed_cache
from ..counts import count_chars, count_words

@typed_cache
def chars_per_word(text: str) -> float:
    """Calculate the average sentence word length in characters.

    This function is a combination of the functions `counts.char_count` and
    `counts.lexicon_count`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The average number of characters per word.

    """
    try:
        return count_chars(text, ignore_spaces=True) / count_words(text)
    except ZeroDivisionError:
        return 0.0
