import cmudict
import syllables

from textstat._filtering import filterable
from textstat.word import Word as BaseWord


class Word(BaseWord):
    __pronunciation_dictionary = cmudict.dict()

    @filterable[int]
    @property
    def syllables(self) -> int:
        pronunciation_syllables = [
            len([part for part in pronunciation if part[-1].isnumeric()])
            for pronunciation in self.__pronunciation_dictionary[self.text.lower()]
        ]
        if pronunciation_syllables:
            return max(pronunciation_syllables)

        return syllables.estimate(self.text.lower())
