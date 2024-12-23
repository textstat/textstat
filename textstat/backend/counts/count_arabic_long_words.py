
import re

from ..utils import typed_cache
from ..transformations import remove_punctuation

@typed_cache
def count_arabic_long_words(text: str) -> int:
    """Counts long arabic words without short vowels (tashkeel).


    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of long arabic words without short vowels (tashkeel).

    """
    tashkeel = (
        r"\u064E|\u064B|\u064F|\u064C|\u0650|\u064D|\u0651|"
        + r"\u0652|\u0653|\u0657|\u0658"
    )
    text = remove_punctuation(
        re.sub(tashkeel, "", text), rm_apostrophe=True
    )

    count = 0
    for t in text.split():
        if len(t) > 5:
            count += 1

    return count
