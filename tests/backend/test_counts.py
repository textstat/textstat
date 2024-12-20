import pytest
import textstat.backend.counts as counts


@pytest.mark.parametrize(
    "text,ignore_spaces,expected",
    [
        ("", True, 0),
        ("", False, 0),
        ("a", True, 1),
        ("a ", True, 1),
        ("a ", False, 2),
        ("a b", True, 2),
        ("a b", False, 3),
        ("a $!&#@*b", True, 8),
        ("a $!&#@*b", False, 9),
    ],
)
def test_char_count(text: str, ignore_spaces: bool, expected: int) -> None:
    assert counts.char_count(text, ignore_spaces) == expected


@pytest.mark.parametrize(
    "text,expected",
    [
        ("", 0),
        ("a", 1),
        ("a ", 1),
        ("a b", 2),
        ("They're here, and they're there.", 24),
        (
            "Who's there?I have no time for this... nonsense...my guy! a who's-who, veritably.",
            57,
        ),
    ],
)
def test_letter_count(text: str, expected: int) -> None:
    assert counts.letter_count(text) == expected


@pytest.mark.parametrize(
    "text,n_words",
    [
        ("", 0),
        ("a", 1),
        ("a ", 1),
        ("a b", 2),
        ("They're here, and they're there.", 5),
        (
            "Who's there?I have no time for this... nonsense...my guy! a who's-who, veritably.",
            12,
        ),
    ],
)
def test_lexicon_count(text: str, n_words: int) -> None:
    assert counts.lexicon_count(text) == n_words
