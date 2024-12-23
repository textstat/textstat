import re

from ..utils._typed_cache import typed_cache


@typed_cache
def count_complex_arabic_words(text: str) -> int:
    """
    Count complex arabic words. Complex arabic words are word with
    more than 5 instances between the following:
    - fatHa
    - tanween fatH
    - dhamma
    - tanween Dhamm
    - kasra
    - tanween kasr
    - shaddah

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
