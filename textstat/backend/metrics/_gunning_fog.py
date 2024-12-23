from ..utils._typed_cache import typed_cache
from ..utils._get_lang_cfg import get_lang_cfg
from ..counts._count_words import count_words
from ..counts._count_difficult_words import count_difficult_words
from ._avg_sentence_length import avg_sentence_length


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
