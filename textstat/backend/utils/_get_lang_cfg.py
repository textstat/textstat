from __future__ import annotations

from .constants import LANG_CONFIGS
from ._get_lang_root import get_lang_root


def get_lang_cfg(lang: str, key: str) -> float:
    """Read as get lang config"""
    lang_root = get_lang_root(lang)
    default = LANG_CONFIGS["en"]
    config = LANG_CONFIGS.get(lang_root, default)
    val = config.get(key, default.get(key))
    if val is None:
        raise ValueError(f"Unknown config key {key}")
    return val
