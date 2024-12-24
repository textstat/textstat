from __future__ import annotations

import pytest
from textstat.backend import counts


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
        # TODO: at least one or two based on the standard strings/texts
    ],
)
def test_count_miniwords(text: str, max_size: int, expected: int) -> None:
    assert counts.count_miniwords(text, max_size) == expected
