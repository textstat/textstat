from __future__ import annotations


from ..transformations._remove_punctuation import remove_punctuation
from ..utils._typed_cache import typed_cache


@typed_cache
def list_words(
    text: str,
    rm_punctuation: bool = True,
    rm_apostrophe: bool = False,
    lowercase: bool = False,
) -> list[str]:
    """Get a list of all words in the text. Words are lowercased and
    punctuation is removed. By default apostrophes are not removed but
    they can be using `rm_apostrophe=True`.

    Parameters
    ----------
    text : str
        A text string.
    rm_apostrophe : bool, optional
        Remove apostrophes. The default is False.

    Returns
    -------
    List[str]
        A list of the words.

    """
    if rm_punctuation:
        text = remove_punctuation(text, rm_apostrophe=rm_apostrophe)
    if lowercase:
        text = text.lower()
    return text.split()
