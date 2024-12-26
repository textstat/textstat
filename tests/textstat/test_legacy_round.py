from __future__ import annotations

from textstat import textstat
import pytest


@pytest.mark.parametrize(
    "num,points,expected",
    [
        (1.234, 0, 1),
        (1.234, 1, 1.2),
        (1.234, 2, 1.23),
        (1.234, 3, 1.234),
        (1.234, 4, 1.234),
        (3.512589, 4, 3.5126),
        (3.512589, 5, 3.51259),
        (3.512589, 6, 3.512589),
        (3.512589, 7, 3.512589),
    ],
)
def test_legacy_round(num: float, points: int, expected: float) -> None:
    # Check default non-rounding behavior
    assert textstat._legacy_round(num) == num

    # Check rounding (note this test covers the set_rounding_points method as well)
    ts = type(textstat)()
    ts.set_rounding(True, points)
    assert ts._legacy_round(num) == expected
    ts.set_rounding(False, points)
    assert ts._legacy_round(num) == num

    # Check rounding (note this test covers the set_rounding method as well)
    ts = type(textstat)()
    ts.set_rounding_points(points)
    assert ts._legacy_round(num) == expected
    ts.set_rounding_points(None)
    assert ts._legacy_round(num) == num
