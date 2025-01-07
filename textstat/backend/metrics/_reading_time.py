from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_chars import count_chars


@typed_cache
def reading_time(text: str, ms_per_char: float) -> float:
    """Calculate reading time (Demberg & Keller, 2008).

    Parameters
    ----------
    text : str
        A text string.
    ms_per_char : float
        The reading speed in milliseconds per character.

    Returns
    -------
    float
        The reading time for `text`.
    """
    return ms_per_char * count_chars(text, ignore_spaces=True) / 1000
