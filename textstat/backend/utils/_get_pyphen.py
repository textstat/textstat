from __future__ import annotations

from pyphen import Pyphen  # type: ignore

from ._typed_cache import typed_cache


@typed_cache
def get_pyphen(lang: str) -> Pyphen:
    return Pyphen(lang=lang)
