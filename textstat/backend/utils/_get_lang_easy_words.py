from __future__ import annotations

import warnings

from ._typed_cache import typed_cache
from ._get_lang_root import get_lang_root
import sys

if sys.version_info < (3, 9):
    import pkg_resources

    def _set_words(lang_root: str) -> set[str]:
        return {
            ln.decode("utf-8").strip()
            for ln in pkg_resources.resource_stream(
                "textstat",
                f"resources/{lang_root}/easy_words.txt",
            )
        }
else:
    import importlib.resources as importlib_resources

    def _set_words(lang_root: str) -> set[str]:
        ref = importlib_resources.files("textstat").joinpath(
            f"resources/{lang_root}/easy_words.txt"
        )
        with ref.open() as f:
            return {ln.strip() for ln in f}


@typed_cache
def get_lang_easy_words(lang: str) -> set[str]:
    """Get the easy words for a given language. If the language is not supported,
    the easy words for english are returned.

    Parameters
    ----------
    lang : str
        The language of the text.

    Returns
    -------
    set[str]
        A set of easy words.
    """
    lang_root = get_lang_root(lang)
    try:
        return _set_words(lang_root)
    except FileNotFoundError:
        warnings.warn(
            f"There is no easy words vocabulary for {lang_root}, using english.",
            Warning,
        )
        return _set_words("en")
