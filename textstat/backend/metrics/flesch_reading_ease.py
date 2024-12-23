
from ..utils import typed_cache, get_lang_root, get_lang_cfg
from . import avg_sentence_length, syllables_per_word

@typed_cache
def flesch_reading_ease(text: str, lang: str) -> float:
    lang_root = get_lang_root(lang)
    sentence_length = avg_sentence_length(text)
    syllables = syllables_per_word(text, lang)

    return (
        get_lang_cfg(lang_root, "fre_base")
        - get_lang_cfg(lang_root, "fre_sentence_length") * sentence_length
        - get_lang_cfg(lang_root, "fre_syll_per_word") * syllables
    )
