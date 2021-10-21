import warnings
import re
import math
from collections import Counter
from typing import Union, List, Set

import pkg_resources
from functools import lru_cache
from pyphen import Pyphen

langs = {
    "en": {  # Default config
        "fre_base": 206.835,
        "fre_sentence_length": 1.015,
        "fre_syll_per_word": 84.6,
        "syllable_threshold": 3,
    },
    "de": {
        # Toni Amstad
        "fre_base": 180,
        "fre_sentence_length": 1,
        "fre_syll_per_word": 58.5,
    },
    "es": {
        # Fernandez Huerta Readability Formula
        "fre_base": 206.84,
        "fre_sentence_length": 1.02,
        "fre_syll_per_word": 0.6,
    },
    "fr": {
        "fre_base": 207,
        "fre_sentence_length": 1.015,
        "fre_syll_per_word": 73.6,
    },
    "it": {
        # Flesch-Vacca
        "fre_base": 217,
        "fre_sentence_length": 1.3,
        "fre_syll_per_word": 0.6,
    },
    "nl": {
        # Flesch-Douma
        "fre_base": 206.835,
        "fre_sentence_length": 0.93,
        "fre_syll_per_word": 77,
    },
    "pl": {
        "syllable_threshold": 4,
    },
    "ru": {
        "fre_base": 206.835,
        "fre_sentence_length": 1.3,
        "fre_syll_per_word": 60.1,
    },
}


def get_grade_suffix(grade: int) -> str:
    """
    Select correct ordinal suffix
    """
    ordinal_map = {1: 'st', 2: 'nd', 3: 'rd'}
    teens_map = {11: 'th', 12: 'th', 13: 'th'}
    return teens_map.get(grade % 100, ordinal_map.get(grade % 10, 'th'))


class textstatistics:
    """Main textstat class with methods to calculate redability indices.

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
    __easy_word_sets = {}
    __round_outputs = True
    __round_points = None
    __rm_apostrophe = True
    text_encoding = "utf-8"

    def __init__(self):
        self.set_lang(self.__lang)

    def _cache_clear(self) -> None:
        caching_methods = [
            method for method in dir(self)
            if callable(getattr(self, method))
            and hasattr(getattr(self, method), "cache_info")
        ]

        for method in caching_methods:
            getattr(self, method).cache_clear()

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
        points = self.__round_points if (
            self.__round_points is not None) else points
        if self.__round_outputs:
            p = 10 ** points
            return float(
                math.floor((number * p) + math.copysign(0.5, number))) / p
        else:
            return number

    def set_rounding(
        self, rounding: bool, points: Union[int, None] = None
    ) -> None:
        """Set the attributes `__round_point` and `__round_outputs`.

        Parameters
        ----------
        rounding : bool
            Whether to round the outputs of all textstat methods.
        points : int or None, optional
            The number of decimal digits for the outputs of all textstat
            methods. The default is None.

        Returns
        -------
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
        self.pyphen = Pyphen(lang=self.__lang)
        self._cache_clear()

    @lru_cache(maxsize=128)
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
        if ignore_spaces:
            text = re.sub(r"\s", "", text)
        return len(text)

    @lru_cache(maxsize=128)
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
        if ignore_spaces:
            text = re.sub(r"\s", "", text)
        return len(self.remove_punctuation(text))

    @lru_cache(maxsize=128)
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
        if self.__rm_apostrophe:
            # remove all punctuation
            punctuation_regex = r"[^\w\s]"
        else:
            # replace single quotation marks with double quotation marks but
            # keep apostrophes in contractions
            text = re.sub(r"\'(?![tsd]\b|ve\b|ll\b|re\b)", '"', text)
            # remove all punctuation except apostrophes
            punctuation_regex = r"[^\w\s\']"

        text = re.sub(punctuation_regex, '', text)
        return text

    @lru_cache(maxsize=128)
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
        if removepunct:
            text = self.remove_punctuation(text)
        count = len(text.split())
        return count

    @lru_cache(maxsize=128)
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
        count = len([word for word in self.remove_punctuation(text).split() if
                     len(word) <= max_size])
        return count

    @lru_cache(maxsize=128)
    def syllable_count(self, text: str, lang: Union[str, None] = None) -> int:
        """Calculate syllable words in a text using pyphen.

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
                DeprecationWarning
            )
        if isinstance(text, bytes):
            text = text.decode(self.text_encoding)

        text = text.lower()
        text = self.remove_punctuation(text)

        if not text:
            return 0

        count = 0
        for word in text.split():
            count += len(self.pyphen.positions(word)) + 1
        return count

    @lru_cache(maxsize=128)
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
        ignore_count = 0
        sentences = re.findall(r'\b[^.!?]+[.!?]*', text, re.UNICODE)
        for sentence in sentences:
            if self.lexicon_count(sentence) <= 2:
                ignore_count += 1
        return max(1, len(sentences) - ignore_count)

    @lru_cache(maxsize=128)
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
        try:
            asl = float(self.lexicon_count(text) / self.sentence_count(text))
            return self._legacy_round(asl, 1)
        except ZeroDivisionError:
            return 0.0

    @lru_cache(maxsize=128)
    def avg_syllables_per_word(
        self, text: str, interval: Union[int, None] = None
    ) -> float:
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
        syllable = self.syllable_count(text)
        words = self.lexicon_count(text)
        try:
            if interval:
                syllables_per_word = float(syllable) * interval / float(words)
            else:
                syllables_per_word = float(syllable) / float(words)
            return self._legacy_round(syllables_per_word, 1)
        except ZeroDivisionError:
            return 0.0

    @lru_cache(maxsize=128)
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
        try:
            letters_per_word = float(
                self.char_count(text) / self.lexicon_count(text))
            return self._legacy_round(letters_per_word, 2)
        except ZeroDivisionError:
            return 0.0

    @lru_cache(maxsize=128)
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
        try:
            letters_per_word = float(
                self.letter_count(text) / self.lexicon_count(text))
            return self._legacy_round(letters_per_word, 2)
        except ZeroDivisionError:
            return 0.0

    @lru_cache(maxsize=128)
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
        try:
            sentence_per_word = float(
                self.sentence_count(text) / self.lexicon_count(text))
            return self._legacy_round(sentence_per_word, 2)
        except ZeroDivisionError:
            return 0.0

    @lru_cache(maxsize=128)
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
        s_count = self.sentence_count(text)

        if s_count < 1:
            return self.lexicon_count(text)

        return float(self.lexicon_count(text) / s_count)

    @lru_cache(maxsize=128)
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
        count = 0

        # fatHa | tanween fatH | dhamma | tanween dhamm
        # | kasra | tanween kasr | shaddah
        pattern = re.compile('[\u064E\u064B\u064F\u064C\u0650\u064D\u0651]')

        for w in text.split():
            if len(pattern.findall(w)) > 5:
                count += 1

        return count

    @lru_cache(maxsize=128)
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
        short_count = 0
        long_count = 0

        # tashkeel: fatha | damma | kasra
        tashkeel = [r'\u064E', r'\u064F', r'\u0650']
        char_list = [c for w in self.remove_punctuation(text).split() for c in
                     w]

        for t in tashkeel:
            for i, c in enumerate(char_list):
                if c != t:
                    continue

                # only if a character is a tashkeel, has a successor
                # and is followed by an alef, waw or yaaA ...
                if (i + 1 < len(char_list) and
                        char_list[i+1] in ['\u0627', '\u0648', '\u064a']):
                    # ... increment long syllable count
                    long_count += 1
                else:
                    short_count += 1

        # stress syllables: tanween fatih | tanween damm | tanween kasr
        # | shadda
        stress_pattern = re.compile(r'[\u064B\u064C\u064D\u0651]')
        stress_count = len(stress_pattern.findall(text))

        if short_count == 0:
            text = re.sub(r'[\u0627\u0649\?\.\!\,\s*]', '', text)
            short_count = len(text) - 2

        return short_count + 2 * (long_count + stress_count)

    @lru_cache(maxsize=128)
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
        count = 0

        # single faseeh char's: hamza nabira | hamza satr | amza waw | Thal
        # | DHaA
        unipattern = re.compile(r'[\u0626\u0621\u0624\u0630\u0638]')

        # double faseeh char's: waw wa alef | waw wa noon
        bipattern = re.compile(r'(\u0648\u0627|\u0648\u0646)')

        for w in text.split():
            faseeh_count = len(unipattern.findall(w)) \
                           + len(bipattern.findall(w))

            if self.count_arabic_syllables(w) > 5 and faseeh_count > 0:
                count += 1

        return count

    @lru_cache(maxsize=128)
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
        tashkeel = r"\u064E|\u064B|\u064F|\u064C|\u0650|\u064D|\u0651|" \
                   + r"\u0652|\u0653|\u0657|\u0658"
        text = self.remove_punctuation(re.sub(tashkeel, "", text))

        count = 0
        for t in text.split():
            if len(t) > 5:
                count += 1

        return count

    @lru_cache(maxsize=128)
    def flesch_reading_ease(self, text: str) -> float:
        sentence_length = self.avg_sentence_length(text)
        s_interval = 100 if self.__get_lang_root() in ['es', 'it'] else None
        syllables_per_word = self.avg_syllables_per_word(text, s_interval)
        flesch = (
            self.__get_lang_cfg("fre_base")
            - float(
                self.__get_lang_cfg("fre_sentence_length") * sentence_length
            )
            - float(
                self.__get_lang_cfg("fre_syll_per_word") * syllables_per_word
            )
        )
        return self._legacy_round(flesch, 2)

    @lru_cache(maxsize=128)
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
        sentence_length = self.avg_sentence_length(text)
        syllables_per_word = self.avg_syllables_per_word(text)
        flesch = (
                float(0.39 * sentence_length)
                + float(11.8 * syllables_per_word)
                - 15.59)
        return self._legacy_round(flesch, 1)

    @lru_cache(maxsize=128)
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
        count = 0
        for word in text.split():
            wrds = self.syllable_count(word)
            if wrds >= 3:
                count += 1
        return count

    @lru_cache(maxsize=128)
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
        sentences = self.sentence_count(text)

        if sentences >= 3:
            try:
                poly_syllab = self.polysyllabcount(text)
                smog = (
                        (1.043 * (30 * (poly_syllab / sentences)) ** .5)
                        + 3.1291)
                return self._legacy_round(smog, 1)
            except ZeroDivisionError:
                return 0.0
        else:
            return 0.0

    @lru_cache(maxsize=128)
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
        letters = self._legacy_round(self.avg_letter_per_word(text) * 100, 2)
        sentences = self._legacy_round(
            self.avg_sentence_per_word(text) * 100, 2)
        coleman = float((0.058 * letters) - (0.296 * sentences) - 15.8)
        return self._legacy_round(coleman, 2)

    @lru_cache(maxsize=128)
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
        chrs = self.char_count(text)
        words = self.lexicon_count(text)
        sentences = self.sentence_count(text)
        try:
            a = float(chrs) / float(words)
            b = float(words) / float(sentences)
            readability = (
                    (4.71 * self._legacy_round(a, 2))
                    + (0.5 * self._legacy_round(b, 2))
                    - 21.43)
            return self._legacy_round(readability, 1)
        except ZeroDivisionError:
            return 0.0

    @lru_cache(maxsize=128)
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
        easy_word = 0
        difficult_word = 0
        text_list = text.split()[:100]

        for word in text_list:
            if self.syllable_count(word) < 3:
                easy_word += 1
            else:
                difficult_word += 1

        text = ' '.join(text_list)

        try:
            number = float(
                (easy_word * 1 + difficult_word * 3)
                / self.sentence_count(text)
            )
        except ZeroDivisionError:
            return 0.0

        if number <= 20:
            number -= 2

        return number / 2

    @lru_cache(maxsize=128)
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
        return len(self.difficult_words_list(text, syllable_threshold))

    @lru_cache(maxsize=128)
    def difficult_words_list(
                self, text: str, syllable_threshold: int = 2
            ) -> List[str]:
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
        List[str]
            DESCRIPTION.

        """
        words = set(re.findall(r"[\w\='‘’]+", text.lower()))
        diff_words = [word for word in words
                      if self.is_difficult_word(word, syllable_threshold)]
        return diff_words

    @lru_cache(maxsize=128)
    def is_difficult_word(
        self, word: str, syllable_threshold: int = 2
    ) -> bool:
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
        easy_word_set = self.__get_lang_easy_words()
        if word in easy_word_set:
            return False
        if self.syllable_count(word) < syllable_threshold:
            return False
        return True

    @lru_cache(maxsize=128)
    def is_easy_word(self, word: str, syllable_threshold: int = 2) -> bool:
        return not self.is_difficult_word(word, syllable_threshold)

    @lru_cache(maxsize=128)
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
        word_count = self.lexicon_count(text)
        count = word_count - self.difficult_words(text, syllable_threshold=0)

        try:
            per_easy_words = float(count) / float(word_count) * 100
        except ZeroDivisionError:
            return 0.0

        per_difficult_words = 100 - per_easy_words

        score = (
                (0.1579 * per_difficult_words)
                + (0.0496 * self.avg_sentence_length(text)))

        if per_difficult_words > 5:
            score += 3.6365
        return self._legacy_round(score, 2)

    @lru_cache(maxsize=128)
    def gunning_fog(self, text: str) -> float:
        try:
            syllable_threshold = self.__get_lang_cfg("syllable_threshold")
            per_diff_words = (
                self.difficult_words(
                    text,
                    syllable_threshold=syllable_threshold)
                / self.lexicon_count(text) * 100)

            grade = 0.4 * (self.avg_sentence_length(text) + per_diff_words)
            return self._legacy_round(grade, 2)
        except ZeroDivisionError:
            return 0.0

    @lru_cache(maxsize=128)
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
        words = text.split()

        words_len = len(words)
        long_words = len([wrd for wrd in words if len(wrd) > 6])
        try:
            per_long_words = (float(long_words) * 100) / words_len
        except ZeroDivisionError:
            return 0.0
        asl = self.avg_sentence_length(text)
        lix = asl + per_long_words

        return self._legacy_round(lix, 2)

    @lru_cache(maxsize=128)
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
        words = self.remove_punctuation(text).split()
        long_words_count = len([wrd for wrd in words if len(wrd) > 6])
        sentences_count = self.sentence_count(text)

        try:
            rix = long_words_count / sentences_count
        except ZeroDivisionError:
            rix = 0.00

        return self._legacy_round(rix, 2)

    @lru_cache(maxsize=128)
    def spache_readability(
        self, text: str, float_output: bool = True
    ) -> Union[float, int]:
        """
        Function to calculate SPACHE readability formula for young readers.
        I/P - a text
        O/P - an int Spache Readability Index/Grade Level
        """
        total_no_of_words = self.lexicon_count(text)
        count_of_sentences = self.sentence_count(text)
        try:
            asl = total_no_of_words / count_of_sentences
            pdw = (self.difficult_words(text) / total_no_of_words) * 100
        except ZeroDivisionError:
            return 0.0
        spache = (0.141 * asl) + (0.086 * pdw) + 0.839
        if not float_output:
            return int(spache)
        else:
            return self._legacy_round(spache, 2)

    @lru_cache(maxsize=128)
    def dale_chall_readability_score_v2(self, text: str) -> float:
        """
        Function to calculate New Dale Chall Readability formula.
        I/P - a text
        O/P - an int Dale Chall Readability Index/Grade Level
        """
        total_no_of_words = self.lexicon_count(text)
        count_of_sentences = self.sentence_count(text)
        try:
            asl = total_no_of_words / count_of_sentences
            pdw = (self.difficult_words(text) / total_no_of_words) * 100
        except ZeroDivisionError:
            return 0.0
        raw_score = 0.1579 * (pdw) + 0.0496 * asl
        adjusted_score = raw_score
        if raw_score > 0.05:
            adjusted_score = raw_score + 3.6365
        return self._legacy_round(adjusted_score, 2)

    @lru_cache(maxsize=128)
    def text_standard(
        self, text: str, float_output: bool = None
    ) -> Union[float, str]:

        grade = []

        # Appending Flesch Kincaid Grade
        lower = self._legacy_round(self.flesch_kincaid_grade(text))
        upper = math.ceil(self.flesch_kincaid_grade(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Flesch Reading Easy
        score = self.flesch_reading_ease(text)
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
        lower = self._legacy_round(self.smog_index(text))
        upper = math.ceil(self.smog_index(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Coleman_Liau_Index
        lower = self._legacy_round(self.coleman_liau_index(text))
        upper = math.ceil(self.coleman_liau_index(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Automated_Readability_Index
        lower = self._legacy_round(self.automated_readability_index(text))
        upper = math.ceil(self.automated_readability_index(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Dale_Chall_Readability_Score
        lower = self._legacy_round(self.dale_chall_readability_score(text))
        upper = math.ceil(self.dale_chall_readability_score(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Linsear_Write_Formula
        lower = self._legacy_round(self.linsear_write_formula(text))
        upper = math.ceil(self.linsear_write_formula(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Appending Gunning Fog Index
        lower = self._legacy_round(self.gunning_fog(text))
        upper = math.ceil(self.gunning_fog(text))
        grade.append(int(lower))
        grade.append(int(upper))

        # Finding the Readability Consensus based upon all the above tests
        d = Counter(grade)
        final_grade = d.most_common(1)
        score = final_grade[0][0]

        if float_output:
            return float(score)
        else:
            lower_score = int(score) - 1
            upper_score = lower_score + 1
            return "{}{} and {}{} grade".format(
                lower_score, get_grade_suffix(lower_score),
                upper_score, get_grade_suffix(upper_score)
            )

    @lru_cache(maxsize=128)
    def reading_time(self, text: str, ms_per_char: float = 14.69) -> float:
        """
        Function to calculate reading time (Demberg & Keller, 2008)
        I/P - a text
        O/P - reading time in second
        """
        words = text.split()
        nchars = map(len, words)
        rt_per_word = map(lambda nchar: nchar * ms_per_char, nchars)
        reading_time = sum(list(rt_per_word))

        return self._legacy_round(reading_time/1000, 2)

    # Spanish readability tests
    @lru_cache(maxsize=128)
    def fernandez_huerta(self, text: str) -> float:
        '''
        Fernandez Huerta readability score
        https://legible.es/blog/lecturabilidad-fernandez-huerta/
        '''
        sentence_length = self.avg_sentence_length(text)
        syllables_per_word = self.avg_syllables_per_word(text)

        f_huerta = (
            206.84 - float(60 * syllables_per_word) -
            float(1.02 * sentence_length))
        return self._legacy_round(f_huerta, 2)

    @lru_cache(maxsize=128)
    def szigriszt_pazos(self, text: str) -> float:
        '''
        Szigriszt Pazos readability score (1992)
        https://legible.es/blog/perspicuidad-szigriszt-pazos/
        '''
        syllables = self.syllable_count(text)
        total_words = self.lexicon_count(text)
        total_sentences = self.sentence_count(text)
        try:
            s_p = (
                self.__get_lang_cfg("fre_base") -
                62.3 * (syllables / total_words)
                - (total_words / total_sentences)
            )
        except ZeroDivisionError:
            return 0.0
        return self._legacy_round(s_p, 2)

    @lru_cache(maxsize=128)
    def gutierrez_polini(self, text: str) -> float:
        '''
        Guttierrez de Polini index
        https://legible.es/blog/comprensibilidad-gutierrez-de-polini/
        '''
        total_words = self.lexicon_count(text)
        total_letters = self.letter_count(text)
        total_sentences = self.sentence_count(text)

        try:
            gut_pol = (
                95.2 - 9.7 * (total_letters / total_words)
                - 0.35 * (total_words / total_sentences)
            )
        except ZeroDivisionError:
            return 0.0
        return self._legacy_round(gut_pol, 2)

    @lru_cache(maxsize=128)
    def crawford(self, text: str) -> float:
        '''
        Crawford index
        https://legible.es/blog/formula-de-crawford/
        '''
        total_sentences = self.sentence_count(text)
        total_words = self.lexicon_count(text)
        total_syllables = self.syllable_count(text)

        # Calculating __ per 100 words
        try:
            sentences_per_words = 100 * (total_sentences / total_words)
            syllables_per_words = 100 * (total_syllables / total_words)
        except ZeroDivisionError:
            return 0.0

        craw_years = (
            -0.205 * sentences_per_words
            + 0.049 * syllables_per_words - 3.407
            )

        return self._legacy_round(craw_years, 1)

    @lru_cache(maxsize=128)
    def osman(self, text: str) -> float:
        '''
        Osman index for Arabic texts
        https://www.aclweb.org/anthology/L16-1038.pdf
        '''

        if not len(text):
            return 0.0

        complex_word_rate = float(self.count_complex_arabic_words(text)) \
            / self.lexicon_count(text)
        long_word_rate = float(self.count_arabic_long_words(text)) \
            / self.lexicon_count(text)
        syllables_per_word = float(self.count_arabic_syllables(text)) \
            / self.lexicon_count(text)
        faseeh_per_word = float(self.count_faseeh(text)) \
            / self.lexicon_count(text)

        osman = 200.791 - (1.015 * self.words_per_sentence(text)) - \
            (24.181 * (complex_word_rate + syllables_per_word
                       + faseeh_per_word + long_word_rate))

        return self._legacy_round(osman, 2)

    @lru_cache(maxsize=128)
    def gulpease_index(self, text: str) -> float:
        '''
        Indice Gulpease Index for Italian texts
        https://it.wikipedia.org/wiki/Indice_Gulpease
        '''

        if len(text) < 1:
            return 0.0

        n_words = float(self.lexicon_count(text))
        return self._legacy_round(
            (300 * self.sentence_count(text) / n_words) -
            (10 * self.char_count(text) / n_words) + 89, 1)

    @lru_cache(maxsize=128)
    def long_word_count(self, text: str) -> int:
        ''' counts words with more than 6 characters '''
        word_list = self.remove_punctuation(text).split()
        return len([w for w in word_list if len(w) > 6])

    @lru_cache(maxsize=128)
    def monosyllabcount(self, text: str) -> int:
        ''' counts monosyllables '''
        word_list = self.remove_punctuation(text).split()
        return len([w for w in word_list if self.syllable_count(w) < 2])

    @lru_cache(maxsize=128)
    def wiener_sachtextformel(self, text: str, variant: int) -> float:
        '''
        Wiener Sachtextformel for readability assessment of German texts

        https://de.wikipedia.org/wiki/Lesbarkeitsindex#Wiener_Sachtextformel
        '''

        if len(text) < 1:
            return 0.0

        n_words = float(self.lexicon_count(text))

        ms = 100 * self.polysyllabcount(text) / n_words
        sl = n_words / self.sentence_count(text)
        iw = 100 * self.long_word_count(text) / n_words
        es = 100 * self.monosyllabcount(text) / n_words

        if variant == 1:
            score = (0.1935 * ms) + (0.1672 * sl) \
                + (0.1297 * iw) - (0.0327 * es) - 0.875
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

    @lru_cache(maxsize=128)
    def mcalpine_eflaw(self, text: str) -> float:
        '''
        McAlpine EFLAW score that asseses the readability of English texts
        for English foreign learners

        https://strainindex.wordpress.com/2009/04/30/mcalpine-eflaw-readability-score/
        '''

        if len(text) < 1:
            return 0.0

        n_words = self.lexicon_count(text)
        n_sentences = self.sentence_count(text)
        n_miniwords = self.miniword_count(text)
        return self._legacy_round((n_words + n_miniwords) / n_sentences, 1)

    def __get_lang_cfg(self, key: str) -> float:
        """ Read as get lang config """
        default = langs.get("en")
        config = langs.get(self.__get_lang_root(), default)
        return config.get(key, default.get(key))

    def __get_lang_root(self) -> str:
        return self.__lang.split("_")[0]

    def __get_lang_easy_words(self) -> Set[str]:
        lang = self.__get_lang_root()
        if lang not in self.__easy_word_sets:
            try:
                easy_word_set = {
                    ln.decode("utf-8").strip()
                    for ln in pkg_resources.resource_stream(
                        "textstat",
                        f"resources/{lang}/easy_words.txt",
                    )
                }
            except FileNotFoundError:
                warnings.warn(
                    "There is no easy words vocabulary for "
                    f"{self.__lang}, using english.",
                    Warning,
                )
                easy_word_set = {
                    ln.decode("utf-8").strip()
                    for ln in pkg_resources.resource_stream(
                        "textstat", "resources/en/easy_words.txt"
                    )
                }
            self.__easy_word_sets[lang] = easy_word_set
        return self.__easy_word_sets[lang]


textstat = textstatistics()
