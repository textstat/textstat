from __future__ import annotations

import re

from ..utils._typed_cache import typed_cache
from ..utils.constants import RE_NONCONTRACTION_APOSTROPHE


@typed_cache
def remove_punctuation(
    text: str,
    rm_apostrophe: bool,
) -> str:
    """Get a copy of the text with punctuation removed.

    If the parameter `rm_apostrophe` is set to True, all punctuation is removed,
    including apostrophes.
    If the parameter `rm_apostrophe` is set to False, punctuation is removed with
    the exception of apostrophes in common English contractions.
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
        # remove non-apostrophe single quotation marks
        text = re.sub(RE_NONCONTRACTION_APOSTROPHE, "", text)
        # remove all punctuation except apostrophes
        punctuation_regex = r"[^\w\s\']"

    text = re.sub(punctuation_regex, "", text)
    return text
