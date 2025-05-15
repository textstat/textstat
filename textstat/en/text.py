import warnings
from math import sqrt

from textstat import core
from textstat.en import mixins
from textstat.en.sentence import Sentence
from textstat.en.word import Word


class Text(mixins.Span, core.Text):
    sentence_class = Sentence

    def flesch_reading_ease(self) -> float:
        """
        Flesch, Rudolph. "A new readability yardstick."
        Journal of applied psychology 32.3 (1948): 221.
        """
        return (
            206.835
            - (1.015 * self.avg("words", per="sentences"))
            - (84.6 * self.avg("syllables", per="words"))
        )

    def flesch_kincaid_grade(self) -> float:
        """
        Kincaid, J. Peter, et al.
        "Derivation of new readability formulas (automated readability index,
        fog count and flesch reading ease formula) for navy enlisted personnel."
        """
        return (
            (0.39 * self.avg("words", per="sentences"))
            + (11.8 * self.avg("syllables", per="words"))
            - 15.59
        )

    def smog(self) -> float:
        """
        https://web.archive.org/web/20150905104444/http://www.harrymclaughlin.com/SMOG.htm
        """
        # TODO: Implement sampling
        if len(self.sentences) < 30:
            warnings.warn(
                "Texts of fewer than 30 sentences are considered statistically "
                "invalid, because the formula was normed on 30-sentence samples."
            )
        return 1.0430 * sqrt(
            len(self.filter(Word.syllables >= 3)) * (30 / len(self.sentences)) + 3.1291
        )

    def smog_grade(self) -> float:
        """Mc Laughlin, G. Harry.
        "SMOG grading-a new readability formula."
        Journal of reading 12.8 (1969): 639-646.
        """
        # TODO: Implement sampling
        if len(self.sentences) < 30:
            warnings.warn(
                "Texts of fewer than 30 sentences are considered statistically "
                "invalid, because the formula was normed on 30-sentence samples."
            )
        return (
            sqrt(len(self.filter(Word.syllables >= 3)) * (30 / len(self.sentences))) + 3
        )

    def coleman_liau_index(self) -> float:
        """
        Coleman, Meri, and Ta Lin Liau.
        "A computer readability formula designed for machine scoring."
        Journal of Applied Psychology 60.2 (1975): 283.
        """
        return (
            (0.0588 * (self.avg("letters", per="words") * 100))
            - (0.296 * (self.avg("sentences", per="words") * 100))
            - 15.8
        )

    def automated_readability_index(self) -> float:
        """
        Senter, R. J., and Edgar A. Smith. "Automated readability index."
        Cincinnati Univ OH, 1967.
        """
        return (
            4.71 * self.avg("characters", per="words")
            + 0.5 * self.avg("words", per="sentences")
            - 21.43
        )

    def linsear_write_formula(self) -> float:
        """
        Klare, George R. "Assessing readability."
        Reading research quarterly (1974): 62-102.
        """
        # TODO: Implement sampling
        easy_points = len(self.filter(Word.syllables < 3)) * 1
        difficult_points = len(self.filter(Word.syllables >= 3)) * 3

        result = (easy_points + difficult_points) / len(self.sentences)

        return result / 2 if result > 20 else (result / 2) - 1

    def dale_chall_readability_score(self) -> float:
        """
        Chall, Jeanne Sternlicht, and Edgar Dale.
        "Readability revisited: The new Dale-Chall readability formula."
        Brookline Books, 1995.
        """
        # TODO: Needs Dale-Chall 3000 word list
        ...

    def dale_chall_readability_score_original(self) -> float:
        """
        Dale, Edgar, and Jeanne S. Chall.
        "A formula for predicting readability: Instructions."
        Educational research bulletin (1948): 37-54.
        """
        # TODO: Needs Dale-Chall 763 word list
        ...

    def gunning_fog(self) -> float:
        """Gunning, Robert. "Technique of clear writing." (1952)."""
        # TODO: Implement sampling
        return 0.4 * (
            self.avg("words", per="sentences")
            + (len(self.filter(Word.syllables >= 3)) / len(self.words)) * 100
        )

    def lix(self) -> float:
        """
        Björnsson, C. H. (1968). Läsbarhet. Stockholm: Liber.
        """
        return (len(self.words) / len(self.sentences)) + (
            len(self.words) / len(self.filter(Word.length > 6) * 100)
        )

    def rix(self) -> float:
        """
        Anderson, Jonathan.
        "Lix and rix: Variations on a little-known readability index."
        Journal of Reading 26.6 (1983): 490-496.
        """
        return len(self.filter(Word.length >= 7)) / len(self.sentences)

    def spache_readability(self) -> float:
        """
        Spache, George.
        "A new readability formula for primary-grade reading materials."
        The Elementary School Journal 53.7 (1953): 410-413.
        """
        # TODO: Needs Dale-Chall 763 word list
        ...
