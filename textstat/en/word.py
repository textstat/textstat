import syllables

try:
    import cmudict
except ImportError:
    cmudict = None

from textstat import core
from textstat.properties import filterableproperty

_pronunciation_dictionary = cmudict.dict() if cmudict else {}


class Word(core.Word):
    @filterableproperty
    def syllables(self) -> int:
        """Returns the number of syllables in the word."""
        if self.text.lower() in _pronunciation_dictionary:
            return max(
                len([part for part in pronunciation if part[-1].isnumeric()])
                for pronunciation in _pronunciation_dictionary[self.text.lower()]
            )

        return syllables.estimate(self.text.lower())
