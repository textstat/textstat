from __future__ import annotations


def get_lang_root(lang: str) -> str:
    """Get the root of a language. For example, "en_US" returns "en".
    If the language is already the root, it is returned as is (e.g. "en").

    Parameters
    ----------
    lang : str
        The language of the text.

    Returns
    -------
    str
        The root of the language.
    """
    if "_" in lang:
        return lang.split("_")[0]
    return lang
