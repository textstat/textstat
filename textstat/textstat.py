from __future__ import annotations

import warnings

from .backend import transformations, validations, selections, counts, metrics, utils


class textstatistics:
    """Main textstat class with methods to calculate readability indices.

    Attributes
    ----------
    text_encoding : str
        Default: "utf-8"
    __lang : str
        Default : "en_US"
    __easy_word_sets (deprecated) : dict
        Dictionary of easy word sets.

        deprecated:: 0.7.6
            This attribute has no effect. It will be removed in version 0.8.0.
    __round_outputs (deprecated) : bool or None
        Whether to round the outputs of all textstat methods. Default: None

        deprecated:: 0.7.6
            This attribute has no effect. It will be removed in version 0.8.0.
    __round_points : int or None
        The number of decimals to use when rounding outputs. If round_points is set to
        None, the outputs will not be rounded. Default: None
    __rm_apostrophe : bool
        If True, the remove_punctuation method will remove the apostrophe in
        contractions along with other punctuation. If False, punctuation is
        removed with the exception of apostrophes in common English contractions.
        Default: True
    """

    __lang = "en_US"
    __easy_word_sets = {}
    __round_outputs = None
    __round_points = None
    __rm_apostrophe = True
    text_encoding = "utf-8"

    def __init__(self):
        self.set_lang(self.__lang)

    def _cache_clear(self) -> None:
        """Clear the cache.

        Parameters
        ----------
        None

        Returns
        -------
        None

        deprecated:: 0.7.6
            This method has no effect due to a caching redesign.
            It will be removed in version 0.8.0.

        """
        warnings.warn(
            "The _cache_clear() method is deprecated and "
            "will be removed in version 0.8.0. "
            "It has no effect due to a caching redesign.",
            DeprecationWarning,
            stacklevel=2,
        )
        pass

    def _legacy_round(self, number: float, points: int | None = None) -> float:
        """Round `number`, unless the attribute `__round_points` is `None`.

        Round floating point outputs for backwards compatibility. Rounding can be
        turned on or off by calling `set_rounding_points`.

        Parameters
        ----------
        number : float
        points (deprecated) : int, optional
            This argument is deprecated and has no effect.

            deprecated:: 0.7.6
                Use set_rounding_points instead.
                It will be removed in version 0.8.0.

        Returns
        -------
        float

        """
        if points is not None:
            warnings.warn(
                "The points argument is deprecated and "
                "will be removed in version 0.8.0. "
                "Use set_rounding_points instead.",
                DeprecationWarning,
                stacklevel=2,
            )
        if self.__round_points is None:
            return number
        return round(number, self.__round_points)

    def set_rounding_points(self, points: int | None) -> None:
        """Set the number of decimal digits for rounding textstat outputs.
        Setting `points` to None will disable rounding.

        Parameters
        ----------
        points : int or None
            The number of decimal digits for the outputs of all textstat
            methods. The default is None (no rounding).

        Returns
        -------
        None

        """
        self.__round_points = points

    def set_rounding(self, rounding: bool, points: int | None = None) -> None:
        """Set the rounding behavior. Setting `rounding` to True will round all
        textstat outputs to the number of decimal digits specified by `points`.
        Setting `rounding` to False will disable rounding as will setting `points`
        to None.

        Parameters
        ----------
        rounding (deprecated) : bool
            Whether to round the outputs of all textstat methods.
        points (deprecated) : int or None, optional
            The number of decimal digits for the outputs of all textstat
            methods. The default is None.

        Returns
        -----
        None.

        deprecated:: 0.7.6
            Use set_rounding_points instead.
            It will be removed in version 0.8.0.

        """
        warnings.warn(
            "set_rounding is deprecated and will be removed in version 0.8.0. "
            "Use set_rounding_points instead",
            DeprecationWarning,
            stacklevel=2,
        )
        if rounding:
            self.__round_points = points
        else:
            self.__round_points = None

    def set_rm_apostrophe(self, rm_apostrophe: bool) -> None:
        """Sets whether other methods should remove apostrophes in common
        English contractions when removing punctuation.

        Parameters
        ----------
        rm_apostrophe : bool
            If True, the remove_punctuation method will remove the apostrophe in
            contractions along with other punctuation. If False, punctuation is
            removed with the exception of apostrophes in common English contractions.

        Returns
        -------
        None.

        """
        self.__rm_apostrophe = rm_apostrophe

    def set_lang(self, lang: str) -> None:
        """Set the language of your text strings.

        The default locale ID is 'en_US'.

        Parameters
        ----------
        lang : str
            A locale ID.

        Returns
        -------
        None.

        """
        self.__lang = lang

    def char_count(self, text: str, ignore_spaces: bool = True) -> int:
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
        return counts.count_chars(text, ignore_spaces)

    def letter_count(self, text: str, ignore_spaces: bool | None = None) -> int:
        """Count letters in a text.

        Parameters
        ----------
        text : str
            A text string.
        ignore_spaces (deprecated) : bool, optional
            Ignore whitespaces if True.

            deprecated:: 0.7.6
                This argument is deprecated and has no effect.
                It will be removed in version 0.8.0.

        Returns
        -------
        int
            The number of letters in text.

        """
        if ignore_spaces is not None:
            warnings.warn(
                "The 'ignore_spaces' argument has been deprecated "
                "and will be removed in version 0.8.0. "
                "This argument has no effect.",
                DeprecationWarning,
                stacklevel=2,
            )
        return counts.count_letters(text)

    def remove_punctuation(self, text: str) -> str:
        """Remove punctuation.

        If the instance attribute `__rm_apostrophe` is set to True, all
        punctuation is removed, including apostrophes.
        If the instance attribute `__rm_apostrophe` is set to False,
        punctuation is removed with the exception of apostrophes in common
        English contractions.
        Hyphens are always removed.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        text : str
            A copy of the input text with punctuation removed.

        """
        return transformations.remove_punctuation(text, self.__rm_apostrophe)

    def lexicon_count(
        self,
        text: str,
        removepunct: bool = True,
        split_contractions: bool = False,
        split_hyphens: bool = False,
    ) -> int:
        """Count the number of words in a text.

        English contractions (e.g. "aren't") and hyphenated words are counted as one
        words by default, but can be counted as multiple words with
        `split_contractions=True` and `split_hyphens=True` respectively. If
        `removepunct` is set to False, "words" with no letters (e.g. " .? ") are
        counted as words.

        Parameters
        ----------
        text : str
            A text string.
        removepunct : bool, optional
            Remove punctuation. The default is True.
        split_contractions : bool, optional
            Split common English contractions. The default is False.
        split_hyphens : bool, optional
            Split hyphenated words. The default is False.

        Returns
        -------
        count : int
            Number of words.

        """
        return counts.count_words(
            text,
            rm_punctuation=removepunct,
            split_contractions=split_contractions,
            split_hyphens=split_hyphens,
        )

    def miniword_count(self, text: str, max_size: int = 3) -> int:
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
        return counts.count_miniwords(text, max_size)

    def syllable_count(self, text: str, lang: str | None = None) -> int:
        """Estimate the number of syllables in a text using Pyphen.

        Parameters
        ----------
        text : str
            A text string.
        lang : str or None
            The language of the text.

            deprecated:: 0.5.7
                This argument is deprecated and has no effect.
                It will be removed in version 0.8.0.

        Returns
        -------
        int
            Number of syllables in `text`.
        """
        if lang:
            warnings.warn(
                "The 'lang' argument has been moved to "
                "'textstat.set_lang(<lang>)'. This argument will be removed "
                "in the future.",
                DeprecationWarning,
                stacklevel=2,
            )

        return counts.count_syllables(text, self.__lang)

    def sentence_count(self, text: str) -> int:
        """Count the sentences in the text.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        int
            Number of sentences in `text`.

        """
        return counts.count_sentences(text)

    def avg_sentence_length(self, text: str) -> float:
        """Calculate the average sentence length in words.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The average sentence length.

        deprecated:: 0.7.6
            Use `words_per_sentence` instead.
            It will be removed in version 0.8.0.

        """
        warnings.warn(
            "The 'avg_sentence_length' method has been deprecated due to being "
            "the same as 'words_per_sentence'. This method will be removed in the"
            "future.",
            DeprecationWarning,
            stacklevel=2,
        )
        return self._legacy_round(metrics.words_per_sentence(text))

    def avg_syllables_per_word(self, text: str, interval: int | None = None) -> float:
        """Get the average number of syllables per `interval` words. If
        `interval` is None, it will be interpreted as 1.

        Parameters
        ----------
        text : str
            A text string.
        interval : int or None, optional
            The interval. The default is None (1).

        Returns
        -------
        float
            The average number of syllables per `interval` words.

        """
        if interval is None:
            interval = 1
        aspw = metrics.syllables_per_word(text, self.__lang)
        aspw *= interval
        return self._legacy_round(aspw)

    def avg_character_per_word(self, text: str) -> float:
        """Calculate the average word length in characters.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The average number of characters per word.

        """
        return self._legacy_round(metrics.chars_per_word(text))

    def avg_letter_per_word(self, text: str) -> float:
        """Calculate the average  word length in letters.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The average number of letters per word.

        """
        return self._legacy_round(metrics.letters_per_word(text))

    def avg_sentence_per_word(self, text: str) -> float:
        """Get the number of sentences per word.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            Number of sentences per word.

        """
        return self._legacy_round(metrics.sentences_per_word(text))

    def words_per_sentence(self, text: str) -> float:
        """Calculate the average number of words per sentence.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The average number of words per sentence.

        """
        return self._legacy_round(metrics.words_per_sentence(text))

    def count_complex_arabic_words(self, text: str) -> int:
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
        return counts.count_complex_arabic_words(text)

    def count_arabic_syllables(self, text: str) -> int:
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
        return counts.count_arabic_syllables(text)

    def count_faseeh(self, text: str) -> int:
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
        return counts.count_faseeh(text)

    def count_arabic_long_words(self, text: str) -> int:
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
        return counts.count_arabic_long_words(text)

    def flesch_reading_ease(self, text: str) -> float:
        """Calculate the Flesch Reading Ease formula.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The Flesch Reading Ease for `text`.
        """
        return self._legacy_round(metrics.flesch_reading_ease(text, self.__lang))

    def flesch_kincaid_grade(self, text: str) -> float:
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
        return self._legacy_round(metrics.flesch_kincaid_grade(text, self.__lang))

    def polysyllabcount(self, text: str) -> int:
        """Count the number of words with three or more syllables.

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
        return counts.count_polysyllable_words(text, self.__lang)

    def smog_index(self, text: str) -> float:
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
        return self._legacy_round(metrics.smog_index(text, self.__lang))

    def coleman_liau_index(self, text: str) -> float:
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
        return self._legacy_round(metrics.coleman_liau_index(text))

    def automated_readability_index(self, text: str) -> float:
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
        return self._legacy_round(metrics.automated_readability_index(text))

    def linsear_write_formula(
        self, text: str, strict_lower: bool = False, strict_upper: bool = True
    ) -> float:
        r"""Calculate the Linsear-Write (Lw) metric.

        Canonically the Lw only uses the first 100 words of text. To disable this
        functionality, set `strict_upper` to False.

        Parameters
        ----------
        text : str
            A text string.
        lang : str
            The language of the text.
        strict_lower : bool, optional
            If True, the Lw is only calculated if the number of words is at least
            100. The default is False.
        strict_upper : bool, optional
            If True, the Lw is only calculated on the first 100 words. The default is
            True.

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
        return self._legacy_round(
            metrics.linsear_write_formula(
                text, self.__lang, strict_lower=strict_lower, strict_upper=strict_upper
            )
        )

    def difficult_words(
        self, text: str, syllable_threshold: int = 2, unique: bool = True
    ) -> int:
        """Count the number of difficult words. By default, counts all words,
        but can be set to count only unique words by using `unique=True`.

        Parameters
        ----------
        text : str
            A text string.
        lang : str
            The language of the text.
        syllable_threshold : int, optional
            The cut-off for the number of syllables difficult words are
            required to have. The default is 2.
        unique : bool, optional
            Count only unique words. The default is True.

        Returns
        -------
        int
            Number of difficult words.

        """
        return counts.count_difficult_words(
            text, self.__lang, syllable_threshold, unique
        )

    def difficult_words_list(
        self, text: str, syllable_threshold: int = 2, unique: bool = True
    ) -> list[str]:
        """Get a list of the difficult words in the text.

        Parameters
        ----------
        text : str
            A text string.
        syllable_threshold : int, optional
            The cut-off for the number of syllables difficult words are
            required to have. The default is 2.
        unique : bool, optional
            Count only unique words. The default is True.

        Returns
        -------
        List[str]
            A list of the words deemed difficult.

        """
        if unique:
            return list(
                selections.set_difficult_words(text, syllable_threshold, self.__lang)
            )
        return selections.list_difficult_words(text, syllable_threshold, self.__lang)

    def is_difficult_word(self, word: str, syllable_threshold: int = 2) -> bool:
        """Return True if `word` is a difficult word.

        The function checks if if the word is in the Dale-Chall list of
        easy words. However, it currently doesn't check if the word is a
        regular inflection of a word in the Dale-Chall list!

        If the word is not a word, is not in the easy words list, or is shorter
        than `syllable_threshold`, the function returns False. Else, True.

        Parameters
        ----------
        word : str
            A word.
        syllable_threshold : int, optional
            Minimum number of syllables a difficult word must have. The
            default is 2.

        Returns
        -------
        bool
            False if the word is not a word (i.e. `word` contains whitespace), is not
            in the easy words list, or is shorter than `syllable_threshold`, else
            True.

        """
        return validations.is_difficult_word(word, syllable_threshold, self.__lang)

    def is_easy_word(self, word: str, syllable_threshold: int = 2) -> bool:
        """Return True if `word` is not a difficult word. See the docstring for
        `is_difficult_word` for details.

        Parameters
        ----------
        word : str
            A word.
        syllable_threshold : int, optional
            Minimum number of syllables a difficult word must have. The
            default is 2.

        Returns
        -------
        bool
            True if the word is a word (no whitespace), is not in the easy words list,
            and is shorter than `syllable_threshold`, else False.

        """
        return (len(word.split()) == 1) and (
            not self.is_difficult_word(word, syllable_threshold)
        )

    def dale_chall_readability_score(self, text: str) -> float:
        r"""Estimate the Dale-Chall readability score.

        Deviations from the original Dale-Chall readability score:
        - For now, regular inflections of words in the Dale-Chall list of easy
          words are counted as difficult words
          (see documentation for `is_difficult_word`). This may change in the
          future.
        - Proper names are also counted as difficult words. This is unlikely to
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
        return self._legacy_round(
            metrics.dale_chall_readability_score(text, self.__lang)
        )

    def gunning_fog(self, text: str) -> float:
        """Calculate the Gunning Fog Index formula.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The Gunning Fog Index for `text`.
        """
        return self._legacy_round(metrics.gunning_fog(text, self.__lang))

    def lix(self, text: str) -> float:
        r"""Calculate the LIX for `text`

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The LIX score for `text`.

        Notes
        -----
        The estimate of the LIX score is calculated as:

        .. math::

            LIX = A/B + A*100/C

        A= Number of words
        B= Number of sentences
        C= Number of long words (More than 6 letters)

        """
        return self._legacy_round(metrics.lix(text))

    def rix(self, text: str) -> float:
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

        """
        return self._legacy_round(metrics.rix(text))

    def spache_readability(self, text: str, float_output: bool = True) -> float | int:
        """Calculate SPACHE readability formula for young readers. If `float_output`
        is True, the function returns a float. Otherwise, it rounds down to an int.

        Parameters
        ----------
        text : str
            A text string.
        float_output : bool, optional
            Whether to return a float or an int. The default is True.

        Returns
        -------
        float or int
            The SPACHE readability score for `text`
        """
        readability_score = metrics.spache_readability(text, self.__lang)
        if float_output:
            return self._legacy_round(readability_score)
        else:
            # TODO: should this be rounded instead of int-ed?
            return int(readability_score)

    def dale_chall_readability_score_v2(self, text: str) -> float:
        """Calculate New Dale Chall Readability formula.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The New Dale Chall Readability Score for `text`
        """
        return self._legacy_round(
            metrics.dale_chall_readability_score_v2(text, self.__lang)
        )

    def text_standard(self, text: str, float_output: bool = False) -> float | str:
        """Calculate the Text Standard for `text`. If `float_output` is True,
        calculates the numerical value. Otherwise, returns a string of the form
        "XX and YY grade" where XX and YY are gotten by rounding the float value
        down and up, respectively.

        Parameters
        ----------
        text : str
            A text string.
        float_output : bool, optional
            Whether to return a float or a string. The default is False.

        Returns
        -------
        float
            The Text Standard for `text`.
        """
        standard_value = metrics.text_standard(text, self.__lang)
        if float_output:
            return self._legacy_round(standard_value)
        else:
            lower_score = int(standard_value) - 1
            upper_score = lower_score + 1
            return "{}{} and {}{} grade".format(
                lower_score,
                utils.get_grade_suffix(lower_score),
                upper_score,
                utils.get_grade_suffix(upper_score),
            )

    def reading_time(self, text: str, ms_per_char: float = 14.69) -> float:
        """Calculate reading time (Demberg & Keller, 2008).

        Parameters
        ----------
        text : str
            A text string.
        ms_per_char : float
            The reading speed in milliseconds per character. The default is 14.69.

        Returns
        -------
        float
            The reading time for `text`.
        """
        return self._legacy_round(metrics.reading_time(text, ms_per_char))

    # Spanish readability tests
    def fernandez_huerta(self, text: str) -> float:
        """Calculate Fernandez Huerta readability score
        https://legible.es/blog/lecturabilidad-fernandez-huerta/

        Parameters
        ----------
        text : str
            A text string.
        lang : str
            The language of the text.

        Returns
        -------
        float
            The Fernandez Huerta readability score for `text`
        """
        return self._legacy_round(metrics.fernandez_huerta(text, self.__lang))

    def szigriszt_pazos(self, text: str) -> float:
        """Calculate Szigriszt Pazos readability score (1992)
        https://legible.es/blog/perspicuidad-szigriszt-pazos/

        Parameters
        ----------
        text : str
            A text string.
        lang : str
            The language of the text.

        Returns
        -------
        float
            The Szigriszt Pazos readability score for `text`
        """
        return self._legacy_round(metrics.szigriszt_pazos(text, self.__lang))

    def gutierrez_polini(self, text: str) -> float:
        """Calculate Guttierrez de Polini index
        https://legible.es/blog/comprensibilidad-gutierrez-de-polini/

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The Gutierrez de Polini index for `text`
        """
        return self._legacy_round(metrics.gutierrez_polini(text))

    def crawford(self, text: str) -> float:
        r"""Calculate the Crawford index for the text.

        https://legible.es/blog/formula-de-crawford/

        Parameters
        ----------
        text : str
            A text string.
        lang : str
            The language of the text.

        Returns
        -------
        float
            The Crawford index for `text`.

        Notes
        -----
        The Crawford index is calculated as:

        .. math::

            (-0.205*n\ sentences/n\ words)+(0.049*n\ syllables/n\ words)-3.407

        """
        return self._legacy_round(metrics.crawford(text, self.__lang))

    def osman(self, text: str) -> float:
        """Calculate Osman index for Arabic texts
        https://www.aclweb.org/anthology/L16-1038.pdf

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The Osman index for `text`
        """
        return self._legacy_round(metrics.osman(text))

    def gulpease_index(self, text: str) -> float:
        """Calculate Indice Gulpease Index for Italian texts
        https://it.wikipedia.org/wiki/Indice_Gulpease

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The Gulpease Index for `text`
        """
        return self._legacy_round(metrics.gulpease_index(text))

    def long_word_count(self, text: str, threshold: int = 6) -> int:
        """Counts words with more than `threshold` (default 6) letters.

        Parameters
        ----------
        text : str
            A text string.
        threshold : int
            The minimum number of letters in a word for it to be counted.

        Returns
        -------
        int
            Number of words with more than `threshold` letters.
        """
        return counts.count_long_words(text, threshold=threshold)

    def monosyllabcount(self, text: str) -> int:
        """Counts words with only one syllable in a text.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        int
        Number of monosyllable words in the text.
        """
        return counts.count_monosyllable_words(text, self.__lang)

    def wiener_sachtextformel(self, text: str, variant: int) -> float:
        """Calculate Wiener Sachtextformel for readability assessment of German texts

        https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel

        Parameters
        ----------
        text : str
            A text string.
        variant : int
            The variant of the formula.

        Returns
        -------
        float
            The Wiener Sachtextformel readability score for `text`
        """
        return self._legacy_round(
            metrics.wiener_sachtextformel(text, variant, self.__lang)
        )

    def mcalpine_eflaw(self, text: str) -> float:
        """Calculate McAlpine EFLAW score, which asseses the readability of English
        texts for English foreign learners.

        https://strainindex.wordpress.com/2009/04/30/mcalpine-eflaw-readability-score/

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The McAlpine EFLAW readability score for `text`
        """
        return self._legacy_round(metrics.mcalpine_eflaw(text))

    def __get_lang_cfg(self, key: str) -> float:
        """Get a value from the configuration for a specific language.

        Parameters
        ----------
        key : str
            The key to retrieve from the configuration.

        Returns
        -------
        float
            The value from the configuration.

        """
        return utils.get_lang_cfg(self.__lang, key)

    def __get_lang_root(self) -> str:
        """Get the root language of a language.

        Parameters
        ----------
        None

        Returns
        -------
        str
            The root language of the given language.
        """
        return utils.get_lang_root(self.__lang)

    def __get_lang_easy_words(self) -> set[str]:
        """Get the easy words for a language.

        Parameters
        ----------
        None

        Returns
        -------
        set[str]
            The easy words for the given language.
        """
        return utils.get_lang_easy_words(self.__lang)


textstat = textstatistics()
