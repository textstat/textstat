from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_letters import count_letters
from ..counts._count_words import count_words


@typed_cache
def letters_per_word(text: str) -> float:
    """Calculate the average word length in letters.

    This function is a combination of the functions `counts.count_letters` and
    `counts.count_words`.

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
        return 0.0
