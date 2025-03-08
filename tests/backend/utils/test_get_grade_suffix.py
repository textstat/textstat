from __future__ import annotations

import pytest
from textstat.backend import utils


@pytest.mark.parametrize(
    "grade, expected",
    [
        (1, "st"),
        (2, "nd"),
        (3, "rd"),
        (4, "th"),
        (5, "th"),
        (6, "th"),
        (7, "th"),
        (8, "th"),
        (9, "th"),
        (10, "th"),
        (11, "th"),
        (12, "th"),
        (13, "th"),
        (14, "th"),
        (15, "th"),
        (16, "th"),
        (17, "th"),
        (20, "th"),
        (21, "st"),
        (101, "st"),
        (4232, "nd"),
        (423, "rd"),
    ],
)
def test_get_grade_suffix(grade: int, expected: str) -> None:
    assert utils.get_grade_suffix(grade) == expected
