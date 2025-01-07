from __future__ import annotations

import pytest
from textstat import textstat
from ..backend import resources


@pytest.mark.parametrize(
    "text, float_output, expected",
    [
        (resources.EMPTY_STR, True, 0.0),
        (resources.EMPTY_STR, False, "-1th and 0th grade"),
        (resources.EASY_TEXT, True, 4.0),
        (resources.EASY_TEXT, False, "3rd and 4th grade"),
        (resources.SHORT_TEXT, True, 2.0),
        (resources.SHORT_TEXT, False, "1st and 2nd grade"),
        (resources.PUNCT_TEXT, True, 6.0),
        (resources.PUNCT_TEXT, False, "5th and 6th grade"),
        (resources.LONG_TEXT, True, 11.0),
        (resources.LONG_TEXT, False, "10th and 11th grade"),
    ],
)
def test_text_standard(text: str, float_output: bool, expected: float | str) -> None:
    ts = type(textstat)()
    assert ts.text_standard(text, float_output) == expected
