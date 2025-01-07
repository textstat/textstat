from __future__ import annotations

import pytest
from textstat.backend import utils


@pytest.mark.parametrize(
    "lang, expected",
    [
        ("en_US", dict),
        ("en_GB", dict),
        ("en", dict),
        ("es", None),
        ("es_ES", None),
        ("de", None),
        ("de_DE", None),
        ("fr", None),
        ("fr_FR", None),
    ],
)
def test_get_cmudict(lang: str, expected: type | None) -> None:
    if expected is None:
        assert utils.get_cmudict(lang) is None
    else:
        assert isinstance(utils.get_cmudict(lang), expected)
