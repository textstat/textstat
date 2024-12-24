from __future__ import annotations

import pytest
from textstat.backend import utils


@pytest.mark.parametrize(
    "lang, root",
    [
        ("en_US", "en"),
        ("en", "en"),
        ("en_GB", "en"),
        ("de_DE", "de"),
        ("es_ES", "es"),
        ("fr_FR", "fr"),
    ],
)
def test_get_lang_root(lang: str, root: str) -> None:
    assert utils.get_lang_root(lang) == root
