
from ..transformations import remove_punctuation
from ..utils import get_pyphen, typed_cache

@typed_cache
def count_syllables(text: str, lang: str) -> int:
    """Calculate syllable words in a text using pyphen.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of syllables in `text`.
    """
    text = text.lower()
    text = remove_punctuation(text, rm_apostrophe=False)

    if not text:
        return 0

    pyphen = get_pyphen(lang)

    return sum([len(pyphen.positions(w)) + 1 for w in text.split()])