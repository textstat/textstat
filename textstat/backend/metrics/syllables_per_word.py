
from ..utils import typed_cache
from ..counts import count_syllables, count_words

@typed_cache
def syllables_per_word(text: str, lang: str) -> float:
    """Get the average number of syllables per word.

    Parameters
    ----------
    text : str
        A text string.
    interval : int or None, optional
        The default is None.

    Returns
    -------
    float
        The average number of syllables per word.

    """
    try:
        return count_syllables(text, lang) / count_words(text)
    except ZeroDivisionError:
        return 0.0
