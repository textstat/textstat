from __future__ import annotations

import pytest
from textstat.backend import counts
from .. import resources


@pytest.mark.parametrize(
    "text,lang,expected",
    [
        ("", "en_US", 0),
        ("a", "en_US", 1),
        ("a ", "en_US", 1),
        ("a b", "en_US", 2),
        ("Where the dog at?", "en_US", 4),
        ("This marriage is an agreement of convenience", "en_US", 11),
        (resources.LONG_TEXT, "en_US", 519),
    ],
)
def test_count_syllables(text: str, lang: str, expected: int) -> None:
    assert counts.count_syllables(text, lang) == expected
