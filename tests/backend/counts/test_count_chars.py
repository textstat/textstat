from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "text,ignore_spaces,expected",
    [
        ("", True, 0),
        ("", False, 0),
        ("a", True, 1),
        ("a ", True, 1),
        ("a ", False, 2),
        ("a b", True, 2),
        ("a b", False, 3),
        ("a $!&#@*b", True, 8),
        ("a $!&#@*b", False, 9),
        (resources.LONG_TEXT, True, 1748),
        (resources.LONG_TEXT, False, 2123),
        (resources.EASY_HUNGARIAN_TEXT, True, 43),
        (resources.EASY_HUNGARIAN_TEXT, False, 54),
    ],
)
def test_count_chars(text: str, ignore_spaces: bool, expected: int) -> None:
    assert counts.count_chars(text, ignore_spaces) == expected
