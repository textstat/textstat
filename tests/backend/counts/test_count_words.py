from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "text, rm_punctuation, split_contractions, split_hyphens, n_words",
    [
        ("", True, False, False, 0),
        ("a", True, False, False, 1),
        ("a ", True, False, False, 1),
        ("a b", True, False, False, 2),
        ("They're here, and they're there.", True, False, False, 5),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            True,
            False,
            False,
            12,
        ),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            True,
            True,
            False,
            14,
        ),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            True,
            True,
            True,
            15,
        ),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            True,
            False,
            True,
            13,
        ),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            False,
            False,
            False,
            13,
        ),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            False,
            True,
            False,
            15,
        ),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            False,
            True,
            True,
            16,
        ),
        (
            """Who's there?I have ... no time for this...
            nonsense...my guy! a who's-who, veritably.""",
            False,
            False,
            True,
            14,
        ),
        (resources.LONG_TEXT, True, False, False, 372),
        (resources.LONG_TEXT, False, False, False, 376),
    ],
)
def test_count_words(
    text: str,
    rm_punctuation: bool,
    split_contractions: bool,
    split_hyphens: bool,
    n_words: int,
) -> None:
    assert (
        counts.count_words(text, rm_punctuation, split_contractions, split_hyphens)
        == n_words
    )
