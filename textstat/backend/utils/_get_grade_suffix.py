def get_grade_suffix(grade: int) -> str:
    """
    Select correct ordinal suffix
    """
    ordinal_map = {1: "st", 2: "nd", 3: "rd"}
    teens_map = {11: "th", 12: "th", 13: "th"}
    return teens_map.get(grade % 100, ordinal_map.get(grade % 10, "th"))
