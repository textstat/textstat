import warnings
from math import sqrt

from textstat.text import Text as BaseText

from .sentence import Sentence
from .word import Word
from .word_collection import WordCollection


class Text(BaseText, WordCollection):
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
        Naval Technical Training Command Millington TN Research Branch, 1975.
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
        ...

    def coleman_liau_index(self) -> float:
        """
        Coleman, Meri, and Ta Lin Liau.
        "A computer readability formula designed for machine scoring."
        Journal of Applied Psychology 60.2 (1975): 283.
        """
        ...

    def automated_readability_index(self) -> float:
        """
        Senter, R. J., and Edgar A. Smith. "Automated readability index."
        Cincinnati Univ OH, 1967.
        """
        ...

    def linsear_write_formula(self) -> float:
        """
        Klare, George R. "Assessing readability."
        Reading research quarterly (1974): 62-102.
        """
        ...

    def dale_chall_readability_score(self) -> float:
        """
        Dale, Edgar, and Jeanne S. Chall.
        "A formula for predicting readability: Instructions."
        Educational research bulletin (1948): 37-54.
        """
        ...

    def dale_chall_readability_score_v2(self) -> float:
        """
        Chall, Jeanne Sternlicht, and Edgar Dale.
        "Readability revisited: The new Dale-Chall readability formula."
        Brookline Books, 1995.
        """
        ...

    def gunning_fog(self) -> float:
        """Gunning, Robert. "Technique of clear writing." (1952)."""
        ...

    def lix(self) -> float:
        """
        Björnsson, C. H. (1968). Läsbarhet. Stockholm: Liber.
        """
        ...

    def rix(self) -> float:
        """
        Anderson, Jonathan.
        "Lix and rix: Variations on a little-known readability index."
        Journal of Reading 26.6 (1983): 490-496.
        """
        ...

    def spache_readability(self) -> float:
        """
        Spache, George.
        "A new readability formula for primary-grade reading materials."
        The Elementary School Journal 53.7 (1953): 410-413.
        """
        ...
