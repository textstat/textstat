from textstat.text import Text as BaseText

from .word_collection import WordCollection


class Text(BaseText, WordCollection):
    def flesch_reading_ease(self) -> float:
        ...

    def flesch_kincaid_grade(self) -> float:
        ...

    def smog_index(self) -> float:
        ...

    def coleman_liau_index(self) -> float:
        ...

    def automated_readability_index(self) -> float:
        ...

    def linsear_write_formula(self) -> float:
        ...

    def dale_chall_readability_score(self) -> float:
        ...

    def gunning_fog(self) -> float:
        ...

    def lix(self) -> float:
        ...

    def rix(self) -> float:
        ...

    def spache_readability(self) -> float:
        ...

    def dale_chall_readability_score_v2(self) -> float:
        ...
