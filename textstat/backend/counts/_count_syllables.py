from __future__ import annotations

from ..selections._list_words import list_words
from ..utils._get_cmudict import get_cmudict
from ..utils._get_pyphen import get_pyphen
from ..utils._typed_cache import typed_cache


@typed_cache
def count_syllables(text: str, lang: str) -> int:
    """Estimate the total number of syllables in a text.
    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.
    Returns
    -------
    int
        Number of syllables in the text.
    """
    if not text:
        return 0
    cmu_dict = get_cmudict(lang)
    pyphen = get_pyphen(lang)
    count = 0
    for word in list_words(text, lowercase=True):
        try:
            cmu_phones = cmu_dict[word][0]
            count += sum(1 for p in cmu_phones if p[-1].isdigit())
        except (TypeError, IndexError, KeyError):
            count += len(pyphen.positions(word)) + 1
    return count
