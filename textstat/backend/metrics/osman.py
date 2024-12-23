
from ..utils import typed_cache
from ..counts import count_words, count_complex_arabic_words, count_arabic_long_words, count_arabic_syllables, count_faseeh
from . import words_per_sentence

@typed_cache
def osman(text: str) -> float:
    """
    Osman index for Arabic texts
    https://www.aclweb.org/anthology/L16-1038.pdf
    """

    if not len(text):
        return 0.0

    complex_word_rate = float(
        count_complex_arabic_words(text)
    ) / count_words(text)
    long_word_rate = float(count_arabic_long_words(text)) / count_words(
        text
    )
    syllables_per_word = float(
        count_arabic_syllables(text)
    ) / count_words(text)
    faseeh_per_word = float(count_faseeh(text)) / count_words(text)

    return (
        200.791
        - (1.015 * words_per_sentence(text))
        - (
            24.181
            * (
                complex_word_rate
                + syllables_per_word
                + faseeh_per_word
                + long_word_rate
            )
        )
    )
