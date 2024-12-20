from __future__ import annotations

import re

from . import transformations
from . import utils
from . import selections


@utils.typed_cache
def char_count(text: str, ignore_spaces: bool) -> int:
    """Count the number of characters in a text.

    Parameters
    ----------
    text : str
        A text string.
    ignore_spaces : bool, optional
        Ignore whitespaces if True. The default is True.

    Returns
    -------
    int
        Number of characters.

    """
    if ignore_spaces:
        text = re.sub(r"\s", "", text)
    return len(text)


@utils.typed_cache
def letter_count(text: str) -> int:
    """Count letters in a text. Spaces are ignored.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        The number of letters in text.

    """
    # Ignore spaces
    text = re.sub(r"\s", "", text)
    return len(transformations.remove_punctuation(text, rm_apostrophe=True))


@utils.typed_cache
def lexicon_count(text: str) -> int:
    """Count types (words) in a text.

    English contractions (e.g. "aren't") are counted as one word.
    Hyphenated words are also counted as a single word
    (e.g. "singer-songwriter").

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    count : int
        DESCRIPTION.

    """
    count = len(text.split())
    return count


@utils.typed_cache
def miniword_count(text: str, max_size: int) -> int:
    """Count common words with `max_size` letters or less in a text.

    Parameters
    ----------
    text : str
        A text string.
    max_size : int, optional
        Maximum number of letters in a word for it to be counted. The
        default is 3.

    Returns
    -------
    count : int

    """
    count = len(
        [
            word
            for word in transformations.remove_punctuation(
                text, rm_apostrophe=True
            ).split()
            if len(word) <= max_size
        ]
    )
    return count


@utils.typed_cache
def syllable_count(text: str, lang: str) -> int:
    """Calculate syllable words in a text using pyphen.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of syllables in `text`.
    """
    text = text.lower()
    text = transformations.remove_punctuation(text, rm_apostrophe=True)

    if not text:
        return 0

    return sum([utils.syllables_in_word(w, lang) for w in text.split()])


@utils.typed_cache
def sentence_count(text: str) -> int:
    """Count the sentences of the text.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of sentences in `text`. Will always be at least 1.

    """
    ignore_count = 0
    sentences = re.findall(r"\b[^.!?]+[.!?]*", text, re.UNICODE)
    for sentence in sentences:
        if lexicon_count(sentence) <= 2:
            ignore_count += 1
    return max(1, len(sentences) - ignore_count)


@utils.typed_cache
def count_complex_arabic_words(text: str) -> int:
    """
    Count complex arabic words.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of arabic complex words.

    """
    count = 0

    # fatHa | tanween fatH | dhamma | tanween dhamm
    # | kasra | tanween kasr | shaddah
    pattern = re.compile("[\u064e\u064b\u064f\u064c\u0650\u064d\u0651]")

    for w in text.split():
        if len(pattern.findall(w)) > 5:
            count += 1

    return count


@utils.typed_cache
def count_arabic_syllables(text: str) -> int:
    """Count arabic syllables.

    Long and stressed syllables are counted double.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of arabic syllables.

    """
    short_count = 0
    long_count = 0

    # tashkeel: fatha | damma | kasra
    tashkeel = [r"\u064E", r"\u064F", r"\u0650"]
    char_list = [
        c
        for w in transformations.remove_punctuation(text, rm_apostrophe=True).split()
        for c in w
    ]

    for t in tashkeel:
        for i, c in enumerate(char_list):
            if c != t:
                continue

            # only if a character is a tashkeel, has a successor
            # and is followed by an alef, waw or yaaA ...
            if i + 1 < len(char_list) and char_list[i + 1] in [
                "\u0627",
                "\u0648",
                "\u064a",
            ]:
                # ... increment long syllable count
                long_count += 1
            else:
                short_count += 1

    # stress syllables: tanween fatih | tanween damm | tanween kasr
    # | shadda
    stress_pattern = re.compile(r"[\u064B\u064C\u064D\u0651]")
    stress_count = len(stress_pattern.findall(text))

    if short_count == 0:
        text = re.sub(r"[\u0627\u0649\?\.\!\,\s*]", "", text)
        short_count = len(text) - 2

    return short_count + 2 * (long_count + stress_count)


@utils.typed_cache
def count_faseeh(text: str) -> int:
    """Counts faseeh in arabic texts.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of faseeh.

    """
    count = 0

    # single faseeh char's: hamza nabira | hamza satr | amza waw | Thal
    # | DHaA
    unipattern = re.compile(r"[\u0626\u0621\u0624\u0630\u0638]")

    # double faseeh char's: waw wa alef | waw wa noon
    bipattern = re.compile(r"(\u0648\u0627|\u0648\u0646)")

    for w in text.split():
        faseeh_count = len(unipattern.findall(w)) + len(bipattern.findall(w))

        if count_arabic_syllables(w) > 5 and faseeh_count > 0:
            count += 1

    return count


@utils.typed_cache
def count_arabic_long_words(text: str) -> int:
    """Counts long arabic words without short vowels (tashkeel).


    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of long arabic words without short vowels (tashkeel).

    """
    tashkeel = (
        r"\u064E|\u064B|\u064F|\u064C|\u0650|\u064D|\u0651|"
        + r"\u0652|\u0653|\u0657|\u0658"
    )
    text = transformations.remove_punctuation(
        re.sub(tashkeel, "", text), rm_apostrophe=True
    )

    count = 0
    for t in text.split():
        if len(t) > 5:
            count += 1

    return count


@utils.typed_cache
def polysyllabcount(text: str, lang: str) -> int:
    """Count the words with three or more syllables.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    int
        Number of words with three or more syllables.

    Notes
    -----
    The function uses text.split() to generate a list of words.
    Contractions and hyphenations are therefore counted as one word.

    """
    count = 0
    for word in text.split():
        wrds = utils.syllables_in_word(word, lang)
        if wrds >= 3:
            count += 1
    return count


@utils.typed_cache
def difficult_words(text: str, lang: str, syllable_threshold: int = 2) -> int:
    """Count the number of difficult words.

    Parameters
    ----------
    text : str
        A text string.
    syllable_threshold : int, optional
        The cut-off for the number of syllables difficult words are
        required to have. The default is 2.

    Returns
    -------
    int
        Number of difficult words.

    """
    return len(selections.difficult_words_list(text, syllable_threshold, lang))


@utils.typed_cache
def long_word_count(text: str) -> int:
    """counts words with more than 6 characters"""
    word_list = transformations.remove_punctuation(text, rm_apostrophe=True).split()
    return len([w for w in word_list if len(w) > 6])


@utils.typed_cache
def monosyllabcount(text: str, lang: str) -> int:
    """counts monosyllables"""
    word_list = transformations.remove_punctuation(text, rm_apostrophe=True).split()
    return len([w for w in word_list if syllable_count(w, lang) < 2])
