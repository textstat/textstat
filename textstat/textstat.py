import warnings

from .backend import transformations, validations, selections, counts, metrics


class textstatistics:
    """Main textstat class with methods to calculate readability indices.

    Attributes
    ----------
    text_encoding : str
        Default: "utf-8"
    __lang : str
        Default : "en_US"
    __round_outputs : bool
        Whether to round floating point outputs. Default: True
    __round_points : int or None
        The number of decimals to use when rounding outputs. round_points will
        override any argument passed to the _legacy_round method. If
        round_points is set to None, the number of decimals will be determined
        by the argument passed to the method. Default: None
    __rm_apostrophe : bool
    """

    __lang = "en_US"
    __round_outputs = True
    __round_points = None
    __rm_apostrophe = True
    text_encoding = "utf-8"

    def __init__(self):
        self.set_lang(self.__lang)

    def _legacy_round(self, number: float, points: int = 0) -> float:
        """Round `number`, unless the attribute `__round_outputs` is `False`.

        Round floating point outputs for backwards compatibility.
        Rounding can be turned off by setting the instance attribute
        `__round_outputs` to False.

        Parameters
        ----------
        number : float
        points : int, optional
            The number of decimal digits to return. If the instance attribute
            `__round_points` is not None, the value of `__round_point` will
            override the value passed for `points`. The default is 0.

        Returns
        -------
        float

        """
        points = self.__round_points if (self.__round_points is not None) else points
        if self.__round_outputs:
            return round(number, points)
        else:
            return number

    def set_rounding(self, rounding: bool, points: int | None = None) -> None:
        """Set the attributes `__round_point` and `__round_outputs`.

        Parameters
        ----------
        rounding : bool
            Whether to round the outputs of all textstat methods.
        points : int or None, optional
            The number of decimal digits for the outputs of all textstat
            methods. The default is None.

        Returns
        -----
        None.

        """
        self.__round_outputs = rounding
        self.__round_points = points

    def set_rm_apostrophe(self, rm_apostrophe: bool) -> None:
        """Set the attribute `__round_point`.

        Parameters
        ----------
        rm_apostrophe : bool
            If True, all textstat methods that use the remove_punctuataion
            function for the word count, syllable count or character count,
            remove the apostrophe in contractions along with other punctuation.
            If False, punctuation is removed with the exception of apostrophes
            in common English contractions.

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
        return counts.char_count(text, ignore_spaces)

    def letter_count(self, text: str, ignore_spaces: bool = True) -> int:
        """Count letters in a text.

        Parameters
        ----------
        text : str
            A text string.
        ignore_spaces : bool, optional
            Ignore whitespaces. The default is True.

        Returns
        -------
        int
            The number of letters in text.

        """
        # TODO: deprecation warning on ignore_spaces
        return counts.letter_count(text)

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
        text : TYPE
            DESCRIPTION.

        """
        return transformations.remove_punctuation(text, self.__rm_apostrophe)

    def lexicon_count(self, text: str, removepunct: bool = True) -> int:
        """Count types (words) in a text.

        If `removepunct` is set to True and
        the instance attribute `__rm_apostrophe` is set to False,
        English contractions (e.g. "aren't") are counted as one word.
        Hyphenated words are counted as a single word
        (e.g. "singer-songwriter").

        Parameters
        ----------
        text : str
            A text string.
        removepunct : bool, optional
            DESCRIPTION. The default is True.

        Returns
        -------
        count : int
            DESCRIPTION.

        """
        # TODO: deprecation warning on removepunct because it never did anything anyway
        return counts.lexicon_count(text)

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
        return counts.miniword_count(text, max_size)

    def syllable_count(self, text: str, lang: str | None = None) -> int:
        """Estimate the number of syllables in a text using Pyphen.

        Parameters
        ----------
        text : str
            A text string.
        lang : str or None
            The language of the text.

            .. deprecated:: 0.5.7

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
            )

        return counts.syllable_count(text, self.__lang)

    def sentence_count(self, text: str) -> int:
        """Count the sentences of the text.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        int
            Number of sentences in `text`.

        """
        return counts.sentence_count(text)

    def avg_sentence_length(self, text: str) -> float:
        """Calculate the average sentence length.

        This function is a combination of the functions `lexicon_count` and
        `sentence_count`.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The average sentence length.

        """
        # TODO: do we really want to round things?
        return self._legacy_round(metrics.avg_sentence_length(text), 1)

    def avg_syllables_per_word(self, text: str, interval: int | None = None) -> float:
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
        aspw = metrics.avg_syllables_per_word(text, self.__lang)
        if interval:
            aspw *= interval
        return self._legacy_round(aspw, 1)

    def avg_character_per_word(self, text: str) -> float:
        """Calculate the average sentence word length in characters.

        This function is a combination of the functions `char_count` and
        `lexicon_count`.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The average number of characters per word.

        """
        return self._legacy_round(metrics.avg_character_per_word(text), 2)

    def avg_letter_per_word(self, text: str) -> float:
        """Calculate the average sentence word length in letters.

        This function is a combination of the functions `letter_count` and
        `lexicon_count`.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The average number of letters per word.

        """
        return self._legacy_round(metrics.avg_letter_per_word(text), 2)

    def avg_sentence_per_word(self, text: str) -> float:
        """Get the number of sentences per word.

        A combination of the functions sentence_count and lecicon_count.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            Number of sentences per word.

        """
        return self._legacy_round(metrics.avg_sentence_per_word(text), 2)

    def words_per_sentence(self, text: str) -> float:
        """Calculate the average number of words per sentence.

        This function is a combination of the functions `lexicon_count` and
        `sentence_count`.

        Parameters
        ----------
        text : str
            A text string.

        Returns
        -------
        float
            The average number of words per sentence.

        """
        # TODO: why no round here?
        return metrics.avg_sentence_per_word(text)

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
        # TODO: method docstring
        return metrics.flesch_reading_ease(text, self.__lang)

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
        return metrics.flesch_kincaid_grade(text, self.__lang)

    def polysyllabcount(self, text: str) -> int:
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
        return counts.polysyllabcount(text, self.__lang)

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
        return metrics.smog_index(text, self.__lang)

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
        return metrics.coleman_liau_index(text)

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
        return metrics.automated_readability_index(text)

    def linsear_write_formula(self, text: str) -> float:
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
        return metrics.linsear_write_formula(text, self.__lang)

    def difficult_words(self, text: str, syllable_threshold: int = 2) -> int:
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
        return counts.difficult_words(text, self.__lang, syllable_threshold)

    def difficult_words_list(self, text: str, syllable_threshold: int = 2) -> list[str]:
        """Get a list of difficult words

        Parameters
        ----------
        text : str
            A text string.
        syllable_threshold : int, optional
            The cut-off for the number of syllables difficult words are
            required to have. The default is 2.

        Returns
        -------
        list[str]
            DESCRIPTION.

        """
        # TODO: need to make the positioning of lang args more consistent (see above)
        return selections.difficult_words_list(text, syllable_threshold, self.__lang)

    def is_difficult_word(self, word: str, syllable_threshold: int = 2) -> bool:
        """Return True if `word` is a difficult word.

        The function checks if if the word is in the Dale-Chall list of
        easy words. However, it currently doesn't check if the word is a
        regular inflection of a word in the Dale-Chall list!

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
            True if the word is not in the easy words list and is longer than
            `syllable_threshold`; else False.

        """
        return validations.is_difficult_word(word, syllable_threshold, self.__lang)

    def is_easy_word(self, word: str, syllable_threshold: int = 2) -> bool:
        return not self.is_difficult_word(word, syllable_threshold)

    def dale_chall_readability_score(self, text: str) -> float:
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
        return metrics.dale_chall_readability_score(text, self.__lang)

    def gunning_fog(self, text: str) -> float:
        # TODO: docstring
        return metrics.gunning_fog(text, self.__lang)

    def lix(self, text: str) -> float:
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
        return metrics.lix(text)

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
        Therefore, make sure to call `textstat.set_rm_apostrophe(False)` before
        calculating the RIX.

        """
        return self._legacy_round(metrics.rix(text), 2)

    def spache_readability(self, text: str, float_output: bool = True) -> float | int:
        """
        Function to calculate SPACHE readability formula for young readers.
        I/P - a text
        O/P - an int Spache Readability Index/Grade Level
        """
        readability_score = metrics.spache_readability(text, self.__lang)
        if float_output:
            return self._legacy_round(readability_score, 2)
        else:
            # TODO
            raise NotImplementedError

    def dale_chall_readability_score_v2(self, text: str) -> float:
        """
        Function to calculate New Dale Chall Readability formula.
        I/P - a text
        O/P - an int Dale Chall Readability Index/Grade Level
        """
        return self._legacy_round(
            metrics.dale_chall_readability_score_v2(text, self.__lang), 2
        )

    def text_standard(self, text: str, float_output: bool = False) -> float | str:
        # TODO: docstring
        standard_value = metrics.text_standard(text, self.__lang)
        if float_output:
            return self._legacy_round(standard_value, 2)
        else:
            # TODO
            raise NotImplementedError

    def reading_time(self, text: str, ms_per_char: float = 14.69) -> float:
        """
        Function to calculate reading time (Demberg & Keller, 2008)
        I/P - a text
        O/P - reading time in second
        """
        return self._legacy_round(metrics.reading_time(text, ms_per_char), 2)

    # Spanish readability tests
    def fernandez_huerta(self, text: str) -> float:
        """
        Fernandez Huerta readability score
        https://legible.es/blog/lecturabilidad-fernandez-huerta/
        """
        return self._legacy_round(metrics.fernandez_huerta(text, self.__lang), 2)

    def szigriszt_pazos(self, text: str) -> float:
        """
        Szigriszt Pazos readability score (1992)
        https://legible.es/blog/perspicuidad-szigriszt-pazos/
        """
        return self._legacy_round(metrics.szigriszt_pazos(text, self.__lang), 2)

    def gutierrez_polini(self, text: str) -> float:
        """
        Guttierrez de Polini index
        https://legible.es/blog/comprensibilidad-gutierrez-de-polini/
        """
        return self._legacy_round(metrics.gutierrez_polini(text), 2)

    def crawford(self, text: str) -> float:
        """
        Crawford index
        https://legible.es/blog/formula-de-crawford/
        """
        return self._legacy_round(metrics.crawford(text, self.__lang), 2)

    def osman(self, text: str) -> float:
        """
        Osman index for Arabic texts
        https://www.aclweb.org/anthology/L16-1038.pdf
        """
        return self._legacy_round(metrics.osman(text), 2)

    def gulpease_index(self, text: str) -> float:
        """
        Indice Gulpease Index for Italian texts
        https://it.wikipedia.org/wiki/Indice_Gulpease
        """
        return self._legacy_round(metrics.gulpease_index(text), 2)

    def long_word_count(self, text: str) -> int:
        """counts words with more than 6 characters"""
        return counts.long_word_count(text)

    def monosyllabcount(self, text: str) -> int:
        """counts monosyllables"""
        return counts.monosyllabcount(text, self.__lang)

    def wiener_sachtextformel(self, text: str, variant: int) -> float:
        """
        Wiener Sachtextformel for readability assessment of German texts

        https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel
        """
        return self._legacy_round(
            metrics.wiener_sachtextformel(text, variant, self.__lang), 1
        )

    def mcalpine_eflaw(self, text: str) -> float:
        """
        McAlpine EFLAW score that asseses the readability of English texts
        for English foreign learners

        https://strainindex.wordpress.com/2009/04/30/mcalpine-eflaw-readability-score/
        """
        return self._legacy_round(metrics.mcalpine_eflaw(text), 1)


textstat = textstatistics()
