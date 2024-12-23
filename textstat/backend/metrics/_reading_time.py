from __future__ import annotations

from ..utils._typed_cache import typed_cache
from ..counts._count_chars import count_chars


@typed_cache
def reading_time(text: str, ms_per_char: float) -> float:
    """
    Function to calculate reading time (Demberg & Keller, 2008)
    I/P - a text
    O/P - reading time in second
    """
    return ms_per_char * count_chars(text, ignore_spaces=True) / 1000
