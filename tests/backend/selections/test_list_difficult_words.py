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
            [],
        ),
        (
            "The quick brown fox jumps over the lazy dog",
            1,
            "en_US",
            ["jumps"],
        ),
        (
            "The quick brown fox jumps over the lazy dog",
            1,
            "en_GB",
            ["jumps"],
        ),
        (
            "The quick brown fox jumps over the lazy dog",
            1,
            "en",
            ["jumps"],
        ),
        (
            "Cool dogs wear da sunglasses.",
            2,
            "en_US",
            ["sunglasses"],
        ),
        (
            "Cool dogs wear da sunglasses.",
            3,
            "en_US",
            ["sunglasses"],
        ),
        (
            "Cool dogs wear da sunglasses.",
            4,
            "en_US",
            [],
        ),
        (
            resources.EASY_TEXT,
            2,
            "en_US",
            [
                "Anna",
                "doing",
                "puzzles",
                "Anna",
                "puzzles",
                "Anna",
                "medium",
                "puzzles",
                "Anna's",
                "puzzles",
                "puzzles",
                "pieces",
                "Anna",
                "puzzles",
                "pieces",
                "puzzles",
                "puzzles",
            ],
        ),
        (
            resources.PUNCT_TEXT,
            2,
            "en_US",
            [
                "remove_punctuation",
                "function",
                "singersongwriter",
                "it'll",
                "suffice",
                "removing",
                "characters",
            ],
        ),
    ],
)
def test_list_difficult_words(
    text: str, syllable_threshold: int, lang: str, expected: list[str]
) -> None:
    assert selections.list_difficult_words(text, syllable_threshold, lang) == expected
