import pytest
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
    ],
)
def test_difficult_words_list(
    text: str, syllable_threshold: int, lang: str, expected: list[str]
) -> None:
    assert selections.difficult_words_list(text, syllable_threshold, lang) == expected
