from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_chars import count_chars
from ..counts._count_words import count_words


@typed_cache
def chars_per_word(text: str, ignore_spaces: bool = True) -> float:
    """Calculate the average word length in characters.

    This function is a combination of the functions `counts.count_chars` and
    `counts.count_words`.

    Parameters
    ----------
    text : str
        A text string.
    ignore_spaces : bool
        whether to include spaces in the character count

    Returns
    -------
    float
        The average number of characters per word.

    """
    # We count puntuation-words as words because those characters get counted
    try:
        return count_chars(text, ignore_spaces=ignore_spaces) / count_words(
            text, rm_punctuation=False
        )
    except ZeroDivisionError:
        return 0.0
