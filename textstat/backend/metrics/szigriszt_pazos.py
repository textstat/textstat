
from ..utils import typed_cache, get_lang_cfg
from ..counts import count_syllables, count_words, count_sentences

@typed_cache
def szigriszt_pazos(text: str, lang: str) -> float:
    """
    Szigriszt Pazos readability score (1992)
    https://legible.es/blog/perspicuidad-szigriszt-pazos/
    """
    syllables = count_syllables(text, lang)
    total_words = count_words(text)
    total_sentences = count_sentences(text)
    try:
        return (
            get_lang_cfg(lang, "fre_base")
            - 62.3 * (syllables / total_words)
            - (total_words / total_sentences)
        )
    except ZeroDivisionError:
        return 0.0

