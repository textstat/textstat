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
        # TODO: test for unknown lang, key, and combo
    ],
)
def test_get_lang_cfg(lang: str, key: str, value: float) -> None:
    assert utils.get_lang_cfg(lang, key) == value
