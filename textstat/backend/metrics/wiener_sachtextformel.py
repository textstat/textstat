
from ..utils import typed_cache
from ..counts import count_words, count_sentences, count_polysyllable_words, count_long_words, count_monosyllable_words

@typed_cache
def wiener_sachtextformel(text: str, variant: int, lang: str) -> float:
    """
    Wiener Sachtextformel for readability assessment of German texts

    https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel
    """

    if len(text) < 1:
        return 0.0

    n_words = float(count_words(text))

    ms = 100 * count_polysyllable_words(text, lang) / n_words
    sl = n_words / count_sentences(text)
    iw = 100 * count_long_words(text) / n_words
    es = 100 * count_monosyllable_words(text, lang) / n_words

    if variant == 1:
        return (0.1935 * ms) + (0.1672 * sl) + (0.1297 * iw) - (0.0327 * es) - 0.875
    elif variant == 2:
        return (0.2007 * ms) + (0.1682 * sl) + (0.1373 * iw) - 2.779
    elif variant == 3:
        return (0.2963 * ms) + (0.1905 * sl) - 1.1144
    elif variant == 4:
        return (0.2744 * ms) + (0.2656 * sl) - 1.693
    else:
        raise ValueError("variant can only be an integer between 1 and 4")
