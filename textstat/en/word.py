import cmudict
import syllables

from textstat import core
from textstat.properties import filterableproperty


class Word(core.Word):
    __pronunciation_dictionary = cmudict.dict()

    @filterableproperty
    def syllables(self) -> int:
        """Returns the number of syllables in the word."""
        if self.text.lower() in self.__pronunciation_dictionary:
            return max(
                len([part for part in pronunciation if part[-1].isnumeric()])
                for pronunciation in self.__pronunciation_dictionary[self.text.lower()]
            )

        return syllables.estimate(self.text.lower())
