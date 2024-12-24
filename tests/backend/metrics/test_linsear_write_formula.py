from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, expected",
    [
        (resources.EMPTY_STR, "en_US", 0.0),
        (resources.EASY_TEXT, "en_US", 4.045),
        (resources.SHORT_TEXT, "en_US", 2.5),
        (resources.PUNCT_TEXT, "en_US", 5.3),
        (resources.LONG_TEXT, "en_US", 14.5),
    ],
)
def test_linsear_write_formula(text: str, lang: str, expected: float) -> None:
    assert round(metrics.linsear_write_formula(text, lang, False, True), 3) == expected
