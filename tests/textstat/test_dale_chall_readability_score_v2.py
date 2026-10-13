from __future__ import annotations

import pytest

from textstat import textstat


@pytest.mark.parametrize(
    "text, words, difficult_words, expected",
    [
        pytest.param(
            "The cat sat on the mat.", 6, 0, 0.2976, id="no-difficult-words"
        ),
        pytest.param(
            "The quizzical cat sat on the mat and watched the dog play by the "
            "tree in the bright warm sun today.",
            21, 1, 1.7935047619, id="below-five-percent"
        ),
        pytest.param(
            "The quizzical cat sat on the mat and watched the dog play by the "
            "tree in the bright warm sun.",
            20, 1, 1.7815, id="exactly-five-percent"
        ),
        pytest.param(
            "The quizzical cat sat on the mat and watched the dog play by the "
            "tree in the warm sun.",
            19, 1, 5.4099526316, id="above-five-percent"
        ),
    ],
)
def test_dale_chall_v2_adjustment_threshold(
    text: str, words: int, difficult_words: int, expected: float
) -> None:
    ts = type(textstat)()
    ts.set_lang("en_US")
    assert ts.lexicon_count(text) == words
    assert ts.difficult_words(text) == difficult_words
    assert ts.dale_chall_readability_score_v2(text) == pytest.approx(expected)
