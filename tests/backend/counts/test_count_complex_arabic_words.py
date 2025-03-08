from __future__ import annotations

import pytest
from textstat.backend import counts


@pytest.mark.parametrize(
    "text,expected",
    [
        # TODO
    ],
)
def test_count_complex_arabic_words(text: str, expected: int) -> None:
    assert counts.count_complex_arabic_words(text) == expected
