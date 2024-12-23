import pkg_resources
import warnings

from ._typed_cache import typed_cache
from ._get_lang_root import get_lang_root


@typed_cache
def get_lang_easy_words(lang: str) -> set[str]:
    lang_root = get_lang_root(lang)
    try:
        return {
            ln.decode("utf-8").strip()
            for ln in pkg_resources.resource_stream(
                "textstat",
                f"resources/{lang_root}/easy_words.txt",
            )
        }
    except FileNotFoundError:
        warnings.warn(
            "There is no easy words vocabulary for " f"{lang_root}, using english.",
            Warning,
        )
        return {
            ln.decode("utf-8").strip()
            for ln in pkg_resources.resource_stream(
                "textstat", "resources/en/easy_words.txt"
            )
        }
