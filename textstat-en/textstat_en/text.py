import warnings
from math import sqrt

from textstat.text import Text as BaseText

from .sentence import Sentence
from .word import Word
from .word_collection import WordCollection


class Text(BaseText, WordCollection):
    sentence_class = Sentence

    def flesch_reading_ease(self) -> float:
        return (
            206.835
            - (1.015 * self.avg("words", per="sentences"))
            - (84.6 * self.avg("syllables", per="words"))
        )

    def flesch_kincaid_grade(self) -> float:
        return (
            (0.39 * self.avg("words", per="sentences"))
            + (11.8 * self.avg("syllables", per="words"))
            - 15.59
        )

    def smog(self) -> float:
        if len(self.sentences) < 30:
            warnings.warn(
                "Texts of fewer than 30 sentences are considered statistically "
                "invalid, because the formula was normed on 30-sentence samples."
            )
        return 1.0430 * sqrt(
            len(self.filter(Word.syllables >= 3)) * (30 / len(self.sentences)) + 3.1291
        )

    def coleman_liau_index(self) -> float:
        ...

    def automated_readability_index(self) -> float:
        ...

    def linsear_write_formula(self) -> float:
        ...

    def dale_chall_readability_score(self) -> float:
        ...

    def dale_chall_readability_score_v2(self) -> float:
        ...

    def gunning_fog(self) -> float:
        ...

    def lix(self) -> float:
        ...

    def rix(self) -> float:
        ...

    def spache_readability(self) -> float:
        ...
