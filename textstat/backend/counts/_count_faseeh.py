import re

from ..utils._typed_cache import typed_cache
from ._count_arabic_syllables import count_arabic_syllables


@typed_cache
def count_faseeh(text: str) -> int:
    """Counts faseeh in arabic texts.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of faseeh.

    """
    count = 0

    # single faseeh char's: hamza nabira | hamza satr | amza waw | Thal
    # | DHaA
    unipattern = re.compile(r"[\u0626\u0621\u0624\u0630\u0638]")

    # double faseeh char's: waw wa alef | waw wa noon
    bipattern = re.compile(r"(\u0648\u0627|\u0648\u0646)")

    for w in text.split():
        faseeh_count = len(unipattern.findall(w)) + len(bipattern.findall(w))

        if count_arabic_syllables(w) > 5 and faseeh_count > 0:
            count += 1

    return count
