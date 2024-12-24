from __future__ import annotations

import pytest
from textstat.backend import counts


@pytest.mark.parametrize(
    "text,expected",
    [
        # TODO
    ],
)
def test_count_faseeh(text: str, expected: int) -> None:
    assert counts.count_faseeh(text) == expected
