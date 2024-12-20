from __future__ import annotations

import math
from collections import Counter

from . import utils
from . import counts


@utils.typed_cache
def avg_sentence_length(text: str) -> float:
    """Calculate the average sentence length.

    This function is a combination of the functions `counts.lexicon_count` and
    `counts.sentence_count`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The average sentence length.

    """
    try:
        return counts.lexicon_count(text) / counts.sentence_count(text)
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def words_per_sentence(text: str) -> float:
    """Calculate the average number of words per sentence.

    This function is a combination of the functions `counts.lexicon_count` and
    `counts.sentence_count`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The average number of words per sentence.

    """
    try:
        return counts.lexicon_count(text) / counts.sentence_count(text)
    except ZeroDivisionError:
        return counts.lexicon_count(text)


@utils.typed_cache
def avg_syllables_per_word(text: str, lang: str) -> float:
    """Get the average number of syllables per word.

    Parameters
    ----------
    text : str
        A text string.
    interval : int or None, optional
        The default is None.

    Returns
    -------
    float
        The average number of syllables per word.

    """
    n_syllable = counts.syllable_count(text, lang)
    try:
        return n_syllable / counts.lexicon_count(text)
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def avg_character_per_word(text: str) -> float:
    """Calculate the average sentence word length in characters.

    This function is a combination of the functions `counts.char_count` and
    `counts.lexicon_count`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The average number of characters per word.

    """
    try:
        return counts.char_count(text, ignore_spaces=True) / counts.lexicon_count(text)
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def avg_letter_per_word(text: str) -> float:
    """Calculate the average sentence word length in letters.

    This function is a combination of the functions `counts.letter_count` and
    `counts.lexicon_count`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The average number of letters per word.

    """
    try:
        return counts.letter_count(text) / counts.lexicon_count(text)
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def avg_sentence_per_word(text: str) -> float:
    """Get the number of sentences per word.

    A combination of the functions counts.sentence_count and lecicon_count.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        Number of sentences per word.

    """
    try:
        return counts.sentence_count(text) / counts.lexicon_count(text)
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def flesch_reading_ease(text: str, lang: str) -> float:
    lang_root = utils.get_lang_root(lang)
    sentence_length = avg_sentence_length(text)
    syllables = avg_syllables_per_word(text, lang)

    return (
        utils.get_lang_cfg(lang_root, "fre_base")
        - utils.get_lang_cfg(lang_root, "fre_sentence_length") * sentence_length
        - utils.get_lang_cfg(lang_root, "fre_syll_per_word") * syllables
    )


@utils.typed_cache
def flesch_kincaid_grade(text: str, lang: str) -> float:
    r"""Calculate the Flesh-Kincaid Grade for `text`.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The Flesh-Kincaid Grade for `text`.

    Notes
    -----
    The Flesh-Kincaid Grade is calculated as:

    .. math::

        (.39*avg\ sentence\ length)+(11.8*avg\ syllables\ per\ word)-15.59

    """
    sentence_length = avg_sentence_length(text)
    syllables_per_word = avg_syllables_per_word(text, lang)
    return (0.39 * sentence_length) + (11.8 * syllables_per_word) - 15.59


@utils.typed_cache
def smog_index(text: str, lang: str) -> float:
    r"""Calculate the SMOG index.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The SMOG index for `text`.

    Notes
    -----
    The SMOG index is calculated as:

    .. math::

        (1.043*(30*(n\ polysyllabic\ words/n\ sentences))^{.5})+3.1291

    Polysyllabic words are defined as words with more than 3 syllables.
    """
    sentences = counts.sentence_count(text)

    if sentences < 3:
        return 0.0

    poly_syllab = counts.polysyllabcount(text, lang)
    try:
        return (1.043 * (30 * (poly_syllab / sentences)) ** 0.5) + 3.1291
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def coleman_liau_index(text: str) -> float:
    r"""Calculate the Coleman-Liaux index.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The Coleman-Liaux index for `text`.

    Notes
    -----
    The Coleman-Liaux index is calculated as:

    .. math::

        (0.058*n\ letters/n\ words)-(0.296*n\ sentences/n\ words)-15.8

    """
    letters = avg_letter_per_word(text) * 100
    sentences = avg_sentence_per_word(text) * 100
    return (0.058 * letters) - (0.296 * sentences) - 15.8


@utils.typed_cache
def automated_readability_index(text: str) -> float:
    r"""Calculate the Automated Readability Index (ARI).

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The ARI for `text`.

    Notes
    -----
    The ARI is calculated as:

    .. math::

        (4.71*n\ characters/n\ words)+(0.5*n\ words/n\ sentences)-21.43

    """
    chrs = counts.char_count(text, True)
    words = counts.lexicon_count(text)
    sentences = counts.sentence_count(text)
    try:
        a = chrs / words
        b = words / sentences
        return (4.71 * a) + (0.5 * b) - 21.43
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def linsear_write_formula(text: str, lang: str) -> float:
    r"""Calculate the Linsear-Write (Lw) metric.

    The Lw only uses the first 100 words of text!

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The Lw for `text`.

    Notes
    -----
    The Lw is calculated using the first 100 words:

    .. math::

        n\ easy\ words+(n\ difficult\ words*3))/n\ sentences

    easy words are defined as words with 2 syllables or less.
    difficult words are defined as words with 3 syllables or more.
    r"""
    easy_word = 0
    difficult_word = 0
    text_list = text.split()[:100]

    for word in text_list:
        if counts.syllable_count(word, lang) < 3:
            easy_word += 1
        else:
            difficult_word += 1

    text = " ".join(text_list)

    try:
        number = float(
            (easy_word * 1 + difficult_word * 3) / counts.sentence_count(text)
        )
    except ZeroDivisionError:
        return 0.0

    if number <= 20:
        number -= 2

    return number / 2


@utils.typed_cache
def dale_chall_readability_score(text: str, lang: str) -> float:
    r"""Estimate the Dale-Chall readability score.

    Deviations from the original Dale-Chall readability score:
    - For now, regular inflections of words in the Dale-Chall list of easy
        words are counted as difficult words
        (see documentation for `is_difficult_word`). This may change in the
        future.
    - Poper names are also counted as difficult words. This is unlikely to
        change.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        An approximation of the Dale-Chall readability score.

    Notes
    -----
    The estimate of the Dale-Chall readability score is calculated as:

    .. math::

        (0.1579*%\ difficult\ words)+(0.0496*avg\ words\ per\ sentence)

    If the percentage of difficult words is > 5, 3.6365 is added to the
    score.
    """
    word_count = counts.lexicon_count(text)
    count = word_count - counts.difficult_words(text, lang, syllable_threshold=0)

    try:
        per_easy_words = float(count) / float(word_count) * 100
    except ZeroDivisionError:
        return 0.0

    per_difficult_words = 100 - per_easy_words

    score = (0.1579 * per_difficult_words) + (0.0496 * avg_sentence_length(text))

    if per_difficult_words > 5:
        score += 3.6365
    return score


@utils.typed_cache
def dale_chall_readability_score_v2(text: str, lang: str) -> float:
    """
    Function to calculate New Dale Chall Readability formula.
    I/P - a text
    O/P - an int Dale Chall Readability Index/Grade Level
    """
    total_no_of_words = counts.lexicon_count(text)
    count_of_sentences = counts.sentence_count(text)
    try:
        asl = total_no_of_words / count_of_sentences
        pdw = (counts.difficult_words(text, lang) / total_no_of_words) * 100
    except ZeroDivisionError:
        return 0.0
    raw_score = 0.1579 * (pdw) + 0.0496 * asl
    adjusted_score = raw_score
    if raw_score > 0.05:
        adjusted_score = raw_score + 3.6365
    return adjusted_score


@utils.typed_cache
def gunning_fog(text: str, lang: str) -> float:
    try:
        syllable_threshold = int(utils.get_lang_cfg(lang, "syllable_threshold"))
        per_diff_words = (
            counts.difficult_words(text, lang, syllable_threshold)
            / counts.lexicon_count(text)
            * 100
        )

        return 0.4 * (avg_sentence_length(text) + per_diff_words)
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def lix(text: str) -> float:
    r"""Calculate the LIX for `text`

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    TYPE
        DESCRIPTION.

    Notes
    -----
    The estimate of the LIX score is calculated as:

    .. math::

        LIX = A/B + A*100/C

    A= Number of words
    B= Number of sentences
    C= Number of long words (More than 6 letters)

    `A` is obtained with `len(text.split())`, which counts
    contractions as one word. `A/B` is
    calculated using the method `textstat.avg_sentence_length()`, which
    counts contractions as two words, unless `__rm_apostrophe` is set to
    False. Therefore, the definition of a word is only consistent if you
    call `textstat.set_rm_apostrophe(False)` before calculating the LIX.

    """
    words = text.split()

    words_len = len(words)
    long_words = len([wrd for wrd in words if len(wrd) > 6])
    try:
        per_long_words = (float(long_words) * 100) / words_len
    except ZeroDivisionError:
        return 0.0
    asl = avg_sentence_length(text)
    return asl + per_long_words


@utils.typed_cache
def rix(text: str) -> float:
    r"""Calculate the RIX for `text`

    A Rix ratio is the number of long words divided by
    the number of assessed sentences.

    Parameters
    ----------
    text : str
        A text string.

    Returns
    -------
    float
        The RIX for `text`.

    Notes
    -----
    The estimate of the RIX score is calculated as:

    .. math::

        rix = LW/S

    LW= Number of long words (i.e. words of 7 or more characters)
    S= Number of sentences

    Anderson (1983) specifies that punctuation should be removed and that
    hyphenated sequences and abbreviations count as single words.
    Therefore, make sure to call `textstat.set_rm_apostrophe(False)` before
    calculating the RIX.

    """
    long_words_count = counts.long_word_count(text)
    sentences_count = counts.sentence_count(text)

    try:
        return long_words_count / sentences_count
    except ZeroDivisionError:
        return 0.00


@utils.typed_cache
def spache_readability(text: str, lang: str) -> float:
    """
    Function to calculate SPACHE readability formula for young readers.
    I/P - a text
    O/P - an int Spache Readability Index/Grade Level
    """
    total_no_of_words = counts.lexicon_count(text)
    count_of_sentences = counts.sentence_count(text)
    try:
        asl = total_no_of_words / count_of_sentences
        pdw = (counts.difficult_words(text, lang) / total_no_of_words) * 100
    except ZeroDivisionError:
        return 0.0
    return (0.141 * asl) + (0.086 * pdw) + 0.839


@utils.typed_cache
def text_standard(text: str, lang: str) -> float:
    grade: list[int] = []

    # Appending Flesch Kincaid Grade
    lower = math.floor(flesch_kincaid_grade(text, lang))
    upper = math.ceil(flesch_kincaid_grade(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Flesch Reading Easy
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
    lower = math.floor(smog_index(text, lang))
    upper = math.ceil(smog_index(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Coleman_Liau_Index
    lower = math.floor(coleman_liau_index(text))
    upper = math.ceil(coleman_liau_index(text))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Automated_Readability_Index
    lower = math.floor(automated_readability_index(text))
    upper = math.ceil(automated_readability_index(text))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Dale_Chall_Readability_Score
    lower = math.floor(dale_chall_readability_score(text, lang))
    upper = math.ceil(dale_chall_readability_score(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Linsear_Write_Formula
    lower = math.floor(linsear_write_formula(text, lang))
    upper = math.ceil(linsear_write_formula(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Appending Gunning Fog Index
    lower = math.floor(gunning_fog(text, lang))
    upper = math.ceil(gunning_fog(text, lang))
    grade.append(int(lower))
    grade.append(int(upper))

    # Finding the Readability Consensus based upon all the above tests
    d = Counter(grade)
    final_grade = d.most_common(1)
    return float(final_grade[0][0])


@utils.typed_cache
def reading_time(text: str, ms_per_char: float) -> float:
    """
    Function to calculate reading time (Demberg & Keller, 2008)
    I/P - a text
    O/P - reading time in second
    """
    words = text.split()
    nchars = map(len, words)
    rt_per_word = map(lambda nchar: nchar * ms_per_char, nchars)
    return sum(list(rt_per_word)) / 1000


# Spanish readability tests
@utils.typed_cache
def fernandez_huerta(text: str, lang: str) -> float:
    """
    Fernandez Huerta readability score
    https://legible.es/blog/lecturabilidad-fernandez-huerta/
    """
    sentence_length = avg_sentence_length(text)
    syllables_per_word = avg_syllables_per_word(text, lang)

    return 206.84 - float(60 * syllables_per_word) - float(1.02 * sentence_length)


@utils.typed_cache
def szigriszt_pazos(text: str, lang: str) -> float:
    """
    Szigriszt Pazos readability score (1992)
    https://legible.es/blog/perspicuidad-szigriszt-pazos/
    """
    syllables = counts.syllable_count(text, lang)
    total_words = counts.lexicon_count(text)
    total_sentences = counts.sentence_count(text)
    try:
        return (
            utils.get_lang_cfg(lang, "fre_base")
            - 62.3 * (syllables / total_words)
            - (total_words / total_sentences)
        )
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def gutierrez_polini(text: str) -> float:
    """
    Guttierrez de Polini index
    https://legible.es/blog/comprensibilidad-gutierrez-de-polini/
    """
    total_words = counts.lexicon_count(text)
    total_letters = counts.letter_count(text)
    total_sentences = counts.sentence_count(text)

    try:
        return (
            95.2
            - 9.7 * (total_letters / total_words)
            - 0.35 * (total_words / total_sentences)
        )
    except ZeroDivisionError:
        return 0.0


@utils.typed_cache
def crawford(text: str, lang: str) -> float:
    """
    Crawford index
    https://legible.es/blog/formula-de-crawford/
    """
    total_sentences = counts.sentence_count(text)
    total_words = counts.lexicon_count(text)
    total_syllables = counts.syllable_count(text, lang)

    # Calculating __ per 100 words
    try:
        sentences_per_words = 100 * (total_sentences / total_words)
        syllables_per_words = 100 * (total_syllables / total_words)
    except ZeroDivisionError:
        return 0.0

    return -0.205 * sentences_per_words + 0.049 * syllables_per_words - 3.407


@utils.typed_cache
def osman(text: str) -> float:
    """
    Osman index for Arabic texts
    https://www.aclweb.org/anthology/L16-1038.pdf
    """

    if not len(text):
        return 0.0

    complex_word_rate = float(
        counts.count_complex_arabic_words(text)
    ) / counts.lexicon_count(text)
    long_word_rate = float(counts.count_arabic_long_words(text)) / counts.lexicon_count(
        text
    )
    syllables_per_word = float(
        counts.count_arabic_syllables(text)
    ) / counts.lexicon_count(text)
    faseeh_per_word = float(counts.count_faseeh(text)) / counts.lexicon_count(text)

    return (
        200.791
        - (1.015 * words_per_sentence(text))
        - (
            24.181
            * (
                complex_word_rate
                + syllables_per_word
                + faseeh_per_word
                + long_word_rate
            )
        )
    )


@utils.typed_cache
def gulpease_index(text: str) -> float:
    """
    Indice Gulpease Index for Italian texts
    https://it.wikipedia.org/wiki/Indice_Gulpease
    """

    if len(text) < 1:
        return 0.0

    return (
        (300 * avg_sentence_per_word(text)) - (10 * avg_character_per_word(text)) + 89
    )


@utils.typed_cache
def wiener_sachtextformel(text: str, variant: int, lang: str) -> float:
    """
    Wiener Sachtextformel for readability assessment of German texts

    https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel
    """

    if len(text) < 1:
        return 0.0

    n_words = float(counts.lexicon_count(text))

    ms = 100 * counts.polysyllabcount(text, lang) / n_words
    sl = n_words / counts.sentence_count(text)
    iw = 100 * counts.long_word_count(text) / n_words
    es = 100 * counts.monosyllabcount(text, lang) / n_words

    if variant == 1:
        score = (0.1935 * ms) + (0.1672 * sl) + (0.1297 * iw) - (0.0327 * es) - 0.875
        return round(score, 1)
    elif variant == 2:
        score = (0.2007 * ms) + (0.1682 * sl) + (0.1373 * iw) - 2.779
        return round(score, 1)
    elif variant == 3:
        score = (0.2963 * ms) + (0.1905 * sl) - 1.1144
        return round(score, 1)
    elif variant == 4:
        score = (0.2744 * ms) + (0.2656 * sl) - 1.693
        return round(score, 1)
    else:
        raise ValueError("variant can only be an integer between 1 and 4")


@utils.typed_cache
def mcalpine_eflaw(text: str) -> float:
    """
    McAlpine EFLAW score that asseses the readability of English texts
    for English foreign learners

    https://strainindex.wordpress.com/2009/04/30/mcalpine-eflaw-readability-score/
    """

    if len(text) < 1:
        return 0.0

    n_words = counts.lexicon_count(text)
    n_sentences = counts.sentence_count(text)
    n_miniwords = counts.miniword_count(text, max_size=3)
    return (n_words + n_miniwords) / n_sentences
