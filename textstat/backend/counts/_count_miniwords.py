from ..utils._typed_cache import typed_cache
from ..transformations._remove_punctuation import remove_punctuation


@typed_cache
def count_miniwords(text: str, max_size: int) -> int:
    """Count common words with `max_size` letters or less in a text.

    Parameters
    ----------
    text : str
        A text string.
    max_size : int, optional
        Maximum number of letters in a word for it to be counted.

    Returns
    -------
    count : int

    """
    count = len(
        [
            word
            for word in remove_punctuation(text, rm_apostrophe=True).split()
            if len(word) <= max_size
        ]
    )
    return count
