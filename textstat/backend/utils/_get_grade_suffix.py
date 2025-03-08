from __future__ import annotations


def get_grade_suffix(grade: int) -> str:
    """Select correct ordinal suffix.

    Parameters
    ----------
    grade : int
        The grade of the text.

    Returns
    -------
    str
        The ordinal suffix.
    """
    ordinal_map = {1: "st", 2: "nd", 3: "rd"}
    teens_map = {11: "th", 12: "th", 13: "th"}
    ordinal_value = grade % 10
    teen_value = grade % 100
    ordinal_suffix = ordinal_map.get(ordinal_value, "th")
    return teens_map.get(teen_value, ordinal_suffix)
