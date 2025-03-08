from __future__ import annotations

from pyphen import Pyphen  # type: ignore

from ._typed_cache import typed_cache


@typed_cache
def get_pyphen(lang: str) -> Pyphen:
    """Get a pyphen object for the given language.

    Parameters
    ----------
    lang : str
        The language of the text.

    Returns
    -------
    Pyphen
        A Pyphen object for the given language.
    """
    return Pyphen(lang=lang)
