from __future__ import annotations

import pytest
from .. import resources
from textstat.backend import selections


@pytest.mark.parametrize(
    "text, syllable_threshold, lang, expected",
    [
        (
            "The quick brown fox jumps over the lazy dog",
            2,
            "en_US",
            set(),
        ),
        (
            "The quick brown fox jumps over the lazy dog",
            1,
            "en_US",
            {"jumps"},
        ),
        (
            "The quick brown fox jumps over the lazy dog",
            1,
            "en_GB",
            {"jumps"},
        ),
        (
            "The quick brown fox jumps over the lazy dog",
            1,
            "en",
            {"jumps"},
        ),
        (
            "Cool dogs wear da sunglasses.",
            2,
            "en_US",
            {"sunglasses"},
        ),
        (
            "Cool dogs wear da sunglasses.",
            3,
            "en_US",
            {"sunglasses"},
        ),
        (
            "Cool dogs wear da sunglasses.",
            4,
            "en_US",
            set(),
        ),
        (
            resources.EASY_TEXT,
            2,
            "en_US",
            {
                "Anna",
                "doing",
                "puzzles",
                "medium",
                "Anna's",
                "pieces",
            },
        ),
        (
            resources.PUNCT_TEXT,
            2,
            "en_US",
            {
                "remove_punctuation",
                "function",
                "singersongwriter",
                "suffice",
                "removing",
                "characters",
                "it'll",
            },
        ),
    ],
)
def test_set_difficult_words(
    text: str, syllable_threshold: int, lang: str, expected: list[str]
) -> None:
    assert selections.set_difficult_words(text, syllable_threshold, lang) == expected
