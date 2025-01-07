from __future__ import annotations

import re

from ..utils._typed_cache import typed_cache


@typed_cache
def count_chars(text: str, ignore_spaces: bool) -> int:
    """Count the number of characters in a text.

    Parameters
    ----------
    text : str
        A text string.
    ignore_spaces : bool, optional
        Ignore whitespaces if True. The default is True.

    Returns
    -------
    int
        Number of characters.

    """
    if ignore_spaces:
        text = re.sub(r"\s", "", text)
    return len(text)
