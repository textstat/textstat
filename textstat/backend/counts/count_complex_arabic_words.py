
import re

from ..utils import typed_cache

@typed_cache
def count_complex_arabic_words(text: str) -> int:
    """
    Count complex arabic words.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of arabic complex words.

    """
    count = 0

    # fatHa | tanween fatH | dhamma | tanween dhamm
    # | kasra | tanween kasr | shaddah
    pattern = re.compile("[\u064e\u064b\u064f\u064c\u0650\u064d\u0651]")

    for w in text.split():
        if len(pattern.findall(w)) > 5:
            count += 1

    return count


