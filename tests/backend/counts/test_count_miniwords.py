from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "text,max_size,expected",
    [
        ("", 1, 0),
        ("a", 1, 1),
        ("a ", 1, 1),
        ("a b", 1, 2),
        ("They're here, and they're there.", 1, 0),
        ("They're here, and they're there.", 2, 0),
        ("They're here, and they're there.", 3, 1),
        ("They're here, and they're there.", 4, 2),
        ("who is me man, I, ye rogue", 1, 1),
        ("who is me man, I, ye rogue", 2, 4),
        ("who is me man, I, ye rogue", 3, 6),
        (resources.EASY_TEXT, 1, 5),
        (resources.EASY_TEXT, 2, 17),
        (resources.EASY_TEXT, 3, 35),
        (resources.EASY_TEXT, 4, 63),
        (resources.PUNCT_TEXT, 3, 23),
        (resources.SHORT_TEXT, 3, 1),
        (resources.LONG_TEXT, 3, 151),
    ],
)
def test_count_miniwords(text: str, max_size: int, expected: int) -> None:
    assert counts.count_miniwords(text, max_size) == expected
