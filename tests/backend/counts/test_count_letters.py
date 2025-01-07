from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),
        ("a", 1),
        ("a ", 1),
        ("a b", 2),
        ("They're here, and they're there.", 24),
        (
            """Who's there?I have no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            57,
        ),
        (resources.LONG_TEXT, 1686),
        (resources.EASY_HUNGARIAN_TEXT, 42),
    ],
)
def test_letter_count(text: str, expected: int) -> None:
    assert counts.count_letters(text) == expected
