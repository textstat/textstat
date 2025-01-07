from __future__ import annotations

from textstat import textstat
import pytest
from ..backend import resources


@pytest.mark.parametrize(
    "rm_apostrophe,expected",
    [
        (True, resources.PUNCT_TEXT_RESULT_WO_APOSTR),
        (False, resources.PUNCT_TEXT_RESULT_W_APOSTR),
    ],
)
def test_set_rm_apostrophe(rm_apostrophe: bool, expected: str) -> None:
    ts = type(textstat)()
    ts.set_rm_apostrophe(rm_apostrophe)
    assert ts.remove_punctuation(resources.PUNCT_TEXT) == expected
