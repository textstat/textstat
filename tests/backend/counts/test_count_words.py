from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "text,removepunct,n_words",
    [
        ("", True, 0),
        ("a", True, 1),
        ("a ", True, 1),
        ("a b", True, 2),
        ("They're here, and they're there.", True, 5),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            True,
            12,
        ),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            False,
            13,
        ),
        (resources.LONG_TEXT, True, 372),
        (resources.LONG_TEXT, False, 376),
    ],
)
def test_count_words(text: str, removepunct: bool, n_words: int) -> None:
    assert counts.count_words(text, removepunct) == n_words
