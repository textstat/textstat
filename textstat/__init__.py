from __future__ import annotations

import types
from typing import TYPE_CHECKING

from textstat import stubs


def __try_import(lang) -> types.ModuleType | None:
    import importlib

    try:
        return importlib.import_module(f"textstat_{lang}")
    except ImportError:
        return None


en: stubs.en = __try_import("en")
