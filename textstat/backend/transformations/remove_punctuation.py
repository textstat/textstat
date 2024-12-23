from __future__ import annotations

import re

from ..utils import typed_cache

@typed_cache
def remove_punctuation(
    text: str,
    rm_apostrophe: bool,
) -> str:
    """Remove punctuation.

    If the parameter `rm_apostrophe` is set to True, all
    punctuation is removed, including apostrophes.
    If the parameter `rm_apostrophe` is set to False,
    punctuation is removed with the exception of apostrophes in common
    English contractions.
    Hyphens are always removed.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    text : str
        A copy of the input text with punctuation removed.

    """
    if rm_apostrophe:
        # remove all punctuation
        punctuation_regex = r"[^\w\s]"
    else:
        # replace single quotation marks with double quotation marks but
        # keep apostrophes in contractions
        text = re.sub(r"\'(?![tsd]\b|ve\b|ll\b|re\b)", '"', text)
        # remove all punctuation except apostrophes
        punctuation_regex = r"[^\w\s\']"

    text = re.sub(punctuation_regex, "", text)
    return text
