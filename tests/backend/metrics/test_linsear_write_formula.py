from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, lang, strict_lower, strict_upper, expected",
    [
        (resources.EMPTY_STR, "en_US", False, False, 0.0),
        (resources.EASY_TEXT, "en_US", False, False, 4.045),
        (resources.EASY_TEXT, "en_US", False, True, 4.045),
        (resources.EASY_TEXT, "en_US", True, False, 0.0),
        (resources.EASY_TEXT, "en_US", True, True, 0.0),
        (resources.SHORT_TEXT, "en_US", False, True, 2.5),
        (resources.PUNCT_TEXT, "en_US", False, True, 5.1),
        (resources.LONG_TEXT, "en_US", False, True, 15.25),
        (resources.LONG_TEXT, "en_US", True, True, 15.25),
    ],
)
def test_linsear_write_formula(
    text: str, lang: str, strict_lower: bool, strict_upper: bool, expected: float
) -> None:
    assert (
        round(
            metrics.linsear_write_formula(
                text, lang, strict_lower=strict_lower, strict_upper=strict_upper
            ),
            3,
        )
        == expected
    )
