from ..utils._typed_cache import typed_cache
from ..transformations._remove_punctuation import remove_punctuation


@typed_cache
def count_words(text: str, removepunct: bool = True) -> int:
    """Count types (words) in a text.

    English contractions (e.g. "aren't") are counted as one word.
    Hyphenated words are also counted as a single word
    (e.g. "singer-songwriter").

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    count : int
        DESCRIPTION.

    """
    # This is useful in the case of "blah [punct] blah"
    if removepunct:
        text = remove_punctuation(text, rm_apostrophe=True)
    count = len(text.split())
    return count
