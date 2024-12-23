
from ..utils import typed_cache, get_lang_cfg
from ..counts import count_words, count_difficult_words
from . import avg_sentence_length

@typed_cache
def gunning_fog(text: str, lang: str) -> float:
    try:
        syllable_threshold = int(get_lang_cfg(lang, "syllable_threshold"))
        per_diff_words = (
            count_difficult_words(text, lang, syllable_threshold)
            / count_words(text)
            * 100
        )

        return 0.4 * (avg_sentence_length(text) + per_diff_words)
    except ZeroDivisionError:
        return 0.0
