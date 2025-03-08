from __future__ import annotations

import cmudict
from ._typed_cache import typed_cache
from ._get_lang_root import get_lang_root


@typed_cache
def get_cmudict(lang: str) -> dict[str, list[list[str]]] | None:
    """Get a cmudict object for the given language. Currently only English is supported.
    Parameters
    ----------
    lang : str
        The language of the text.
    Returns
    -------
    dict[str, list[list[str]]] | None
        A cmudict object for the given language (or None if the language is not
        supported).
    """
    if get_lang_root(lang) == "en":
        return cmudict.dict()
    else:
        return None
