import pytest
import textstat.backend.counts as counts


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
