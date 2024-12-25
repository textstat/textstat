from __future__ import annotations

import importlib.resources as importlib_resources
import warnings

from ._typed_cache import typed_cache
from ._get_lang_root import get_lang_root


@typed_cache
def get_lang_easy_words(lang: str) -> set[str]:
    lang_root = get_lang_root(lang)
    try:
        ref = importlib_resources.files("textstat").joinpath(
            f"resources/{lang_root}/easy_words.txt"
        )
        with ref.open() as f:
            return {ln.strip() for ln in f}
    except FileNotFoundError:
        warnings.warn(
            "There is no easy words vocabulary for " f"{lang_root}, using english.",
            Warning,
        )
        ref = importlib_resources.files("textstat").joinpath(
            "resources/en/easy_words.txt"
        )
        with ref.open() as f:
            return {ln.strip() for ln in f}
