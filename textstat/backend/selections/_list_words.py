from __future__ import annotations
import re


from ..transformations._remove_punctuation import remove_punctuation
from ..utils._typed_cache import typed_cache
from ..utils.constants import RE_CONTRACTION_APOSTROPHE


@typed_cache
def list_words(
    text: str,
    rm_punctuation: bool = True,
    rm_apostrophe: bool = False,
    lowercase: bool = False,
    split_contractions: bool = False,
    split_hyphens: bool = False,
) -> list[str]:
    """Get a list of all words in the text. If specified by args, words can be
    lowercased and punctuation removed. By default apostrophes are not removed with
    other punctuation but they can be by using `rm_apostrophe=True`. If
    `split_contractions` is set to True, contractions are counted as multiple words.
    If `rm_punctuation`, `rm_apostrophe`, and `split_contractions` are all set to
    True, `split_contractions` is ignored. If `split_hyphens` is set to True,
    hyphenated words are counted as multiple words (regardless of `rm_punctuation`).

    Parameters
    ----------
    text : str
        A text string.
    rm_punctuation : bool, optional
        Remove punctuation. The default is True.
    rm_apostrophe : bool, optional
        Remove apostrophes. The default is False.
    lowercase : bool, optional
        Lowercase words. The default is False.
    split_contractions : bool, optional
        Split contractions. The default is False.
    split_hyphens : bool, optional
        Split hyphens. The default is False.

    Returns
    -------
    List[str]
        A list of the words.

    """
    if split_hyphens:
        text = re.sub(r"-", " ", text)
    if rm_punctuation:
        text = remove_punctuation(text, rm_apostrophe=rm_apostrophe)
    if lowercase:
        text = text.lower()
    if split_contractions:
        text = re.sub(RE_CONTRACTION_APOSTROPHE, " ", text)
    return text.split()
