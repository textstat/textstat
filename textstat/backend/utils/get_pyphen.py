

from pyphen import Pyphen  # type: ignore

from . import typed_cache

@typed_cache
def get_pyphen(lang: str) -> Pyphen:
    return Pyphen(lang=lang)

