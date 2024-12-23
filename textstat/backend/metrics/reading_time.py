
from ..utils import typed_cache

@typed_cache
def reading_time(text: str, ms_per_char: float) -> float:
    """
    Function to calculate reading time (Demberg & Keller, 2008)
    I/P - a text
    O/P - reading time in second
    """
    words = text.split()
    nchars = map(len, words)
    rt_per_word = map(lambda nchar: nchar * ms_per_char, nchars)
    return sum(list(rt_per_word)) / 1000
