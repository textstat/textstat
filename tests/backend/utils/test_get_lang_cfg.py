from __future__ import annotations

import pytest
from textstat.backend import utils


@pytest.mark.parametrize(
    "lang, key, value",
    [
        (lang, key, utils.constants.LANG_CONFIGS[lang][key])
        for lang in utils.constants.LANG_CONFIGS
        for key in utils.constants.LANG_CONFIGS[lang]
    ]
    + [
        ("ua_UA", "fre_base", utils.constants.LANG_CONFIGS["en"]["fre_base"]),
    ],
)
def test_get_lang_cfg(lang: str, key: str, value: float) -> None:
    assert utils.get_lang_cfg(lang, key) == value


@pytest.mark.parametrize(
    "lang, key, error",
    [
        ("en_US", "fre_base", False),
        ("en_US", "a;lskdj", True),
        ("sladfjk", "fre_base", False),
        ("sladfjk", "fjksd", True),
    ],
)
def test_get_lang_cfg_error(lang: str, key: str, error: bool) -> None:
    if error:
        with pytest.raises(ValueError):
            utils.get_lang_cfg(lang, key)
    else:
        utils.get_lang_cfg(lang, key)
