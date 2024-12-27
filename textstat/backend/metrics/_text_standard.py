from __future__ import annotations

import math
from collections import Counter

from ..utils._typed_cache import typed_cache
from ._flesch_kincaid_grade import flesch_kincaid_grade
from ._flesch_reading_ease import flesch_reading_ease
from ._smog_index import smog_index
from ._coleman_liau_index import coleman_liau_index
from ._automated_readability_index import automated_readability_index
from ._dale_chall_readability_score import dale_chall_readability_score
from ._linsear_write_formula import linsear_write_formula
from ._gunning_fog import gunning_fog


@typed_cache
def text_standard(text: str, lang: str) -> float:
    """Calculate the Text Standard for `text`. This function specifically calculates
    the numerical value.

    Parameters
    ----------
    text : str
        A text string.
    lang : str
        The language of the text.

    Returns
    -------
    float
        The Text Standard for `text`.
    """
    grade: list[int] = []

    # Appending Flesch Kincaid Grade
    score = flesch_kincaid_grade(text, lang)
    lower = math.floor(score)
    upper = math.ceil(score)
    near = round(score)
    grade.extend([lower, upper, near])

    # Appending Flesch Reading Ease
    score = flesch_reading_ease(text, lang)
    if score < 100 and score >= 90:
        grade.append(5)
    elif score < 90 and score >= 80:
        grade.append(6)
    elif score < 80 and score >= 70:
        grade.append(7)
    elif score < 70 and score >= 60:
        grade.append(8)
        grade.append(9)
    elif score < 60 and score >= 50:
        grade.append(10)
    elif score < 50 and score >= 40:
        grade.append(11)
    elif score < 40 and score >= 30:
        grade.append(12)
    else:
        grade.append(13)

    # Appending SMOG Index
    score = smog_index(text, lang)
    lower = math.floor(score)
    upper = math.ceil(score)
    near = round(score)
    grade.extend([lower, upper, near])

    # Appending Coleman_Liau_Index
    score = coleman_liau_index(text)
    lower = math.floor(score)
    upper = math.ceil(score)
    near = round(score)
    grade.extend([lower, upper, near])

    # Appending Automated_Readability_Index
    score = automated_readability_index(text)
    lower = math.floor(score)
    upper = math.ceil(score)
    near = round(score)
    grade.extend([lower, upper, near])

    # Appending Dale_Chall_Readability_Score
    score = dale_chall_readability_score(text, lang)
    lower = math.floor(score)
    upper = math.ceil(score)
    near = round(score)
    grade.extend([lower, upper, near])

    # Appending Linsear_Write_Formula
    score = linsear_write_formula(text, lang, strict_lower=False, strict_upper=True)
    lower = math.floor(score)
    upper = math.ceil(score)
    near = round(score)
    grade.extend([lower, upper, near])

    # Appending Gunning Fog Index
    score = gunning_fog(text, lang)
    lower = math.floor(score)
    upper = math.ceil(score)
    near = round(score)
    grade.extend([lower, upper, near])

    # Finding the Readability Consensus based upon all the above tests
    d = Counter(grade)
    final_grade = d.most_common(1)
    return float(final_grade[0][0])
