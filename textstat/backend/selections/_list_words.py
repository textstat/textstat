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
    """Get a list of all words in the text. If specified by args, words can be
    lowercased and punctuation removed. By default apostrophes are not removed with
    other punctuation but they can be by using `rm_apostrophe=True`.

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
