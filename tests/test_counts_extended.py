"""Extended coverage for textstat's counting helpers.

The upstream suite tests most counters only through one or two fixed
texts; this file pins the boundary behaviour: empty input, the
space/digit/punctuation rules, the sentence-fragment filter, and the
deprecated-argument warnings. All expected values were produced by a
probe script against the cloned source.

Sample text used throughout (14 words, 2 sentences):
"The quick brown fox jumps over the lazy dog. It was a bright day."
"""

import pytest

from textstat import textstat

SAMPLE = "The quick brown fox jumps over the lazy dog. It was a bright day."


# ---------------------------------------------------------------- char/letter


@pytest.mark.parametrize(
    ("text", "ignore_spaces", "expected"),
    [
        (SAMPLE, True, 52),
        (SAMPLE, False, 65),
        ("", True, 0),
        ("abc 123 !@#", True, 9),  # digits and punctuation count as characters
        ("abc 123 !@#", False, 11),
        ("   ", True, 0),
        ("   ", False, 3),
    ],
)
def test_char_count(text, ignore_spaces, expected):
    assert textstat.char_count(text, ignore_spaces=ignore_spaces) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (SAMPLE, 50),
        ("", 0),
        # Quirk pinned as-is: "letters" here means "characters left after
        # removing spaces and punctuation", so digits still count.
        ("abc 123 !@#", 6),  # abc + 123; punctuation excluded
        ("123 !@#", 3),  # digits count, punctuation does not
        ("!!!", 0),
    ],
)
def test_letter_count(text, expected):
    assert textstat.letter_count(text) == expected


def test_letter_count_ignore_spaces_argument_warns_but_is_ignored():
    with pytest.warns(DeprecationWarning):
        result = textstat.letter_count(SAMPLE, ignore_spaces=False)
    assert result == 50


# ---------------------------------------------------------------- punctuation/lexicon


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hello, world! It's fine.", "Hello world Its fine"),
        ("well-known fact", "wellknown fact"),  # hyphens are always removed
        ("", ""),
        ("no punctuation", "no punctuation"),
    ],
)
def test_remove_punctuation(text, expected):
    assert textstat.remove_punctuation(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (SAMPLE, 14),
        ("", 0),
        ("I have 3 apples", 4),  # numbers count as words
        ("well-known fact", 2),  # hyphenated words count as one word
    ],
)
def test_lexicon_count(text, expected):
    assert textstat.lexicon_count(text) == expected


def test_lexicon_count_removepunct_flag_does_not_change_plain_text():
    assert textstat.lexicon_count(SAMPLE, removepunct=False) == 14


# ---------------------------------------------------------------- mini/long words


@pytest.mark.parametrize(
    ("max_size", "expected"),
    [
        (3, 8),  # words of <= 3 letters in SAMPLE
        (2, 2),
        (1, 1),  # only "a"
    ],
)
def test_miniword_count_thresholds(max_size, expected):
    assert textstat.miniword_count(SAMPLE, max_size=max_size) == expected


def test_miniword_count_empty_text():
    assert textstat.miniword_count("") == 0


@pytest.mark.parametrize(
    ("threshold", "expected"),
    [
        (6, 0),  # no SAMPLE word is longer than 6 letters
        (4, 4),  # quick, brown, jumps, bright
    ],
)
def test_long_word_count_thresholds(threshold, expected):
    assert textstat.long_word_count(SAMPLE, threshold=threshold) == expected


def test_long_word_count_empty_text():
    assert textstat.long_word_count("") == 0


# ---------------------------------------------------------------- sentences/averages


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        (SAMPLE, 2),
        ("", 0),
        ("hello world", 1),  # no terminator: still counts as one sentence
        ("One two three. Four five six. Seven eight nine.", 3),
    ],
)
def test_sentence_count(text, expected):
    assert textstat.sentence_count(text) == expected


def test_sentence_count_drops_fragments_of_two_words_or_fewer():
    # Quirk pinned as-is: count_sentences() discards any fragment with
    # <= 2 words, then floors the result at 1.
    assert textstat.sentence_count("Dr. Smith went home. He slept.") == 1
    assert textstat.sentence_count("Wait... Really? Yes!") == 1


def test_words_per_sentence_and_averages():
    assert textstat.words_per_sentence(SAMPLE) == 7.0
    assert textstat.avg_character_per_word(SAMPLE) == pytest.approx(3.7142857142857144)
    assert textstat.avg_letter_per_word(SAMPLE) == pytest.approx(3.5714285714285716)
    assert textstat.avg_sentence_per_word(SAMPLE) == pytest.approx(0.14285714285714285)


def test_avg_sentence_length_is_words_per_sentence_with_a_warning():
    with pytest.warns(DeprecationWarning):
        assert textstat.avg_sentence_length(SAMPLE) == 7.0
