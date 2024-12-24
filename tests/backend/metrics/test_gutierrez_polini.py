from __future__ import annotations

import pytest

from textstat.backend import metrics
from .. import resources


@pytest.mark.parametrize(
    "text, expected",
    [
        (resources.EMPTY_STR, 0.0),
        (resources.EASY_TEXT, 51.094),
        (resources.SHORT_TEXT, 46.89),
        (resources.PUNCT_TEXT, 49.945),
        (resources.LONG_TEXT, 43.578),
        (resources.EASY_SPANISH_TEXT, 64.35),
    ],
)
def test_gutierrez_polini(text: str, expected: float) -> None:
    assert round(metrics.gutierrez_polini(text), 3) == expected
