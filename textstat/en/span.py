from __future__ import annotations

from textstat import core
from textstat.en.word import Word
from textstat.properties import filterabletextproperty


class Span(core.Span):
    word_class = Word

    @property
    def reading_time(self) -> float:
        """Calculates the reading time, based on:
        https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.685.9115&rep=rep1&type=pdf
        """
        total: float = 0.0

        word_base_ms = 275  # INTERCEPT
        character_ms = 14.69  # WORDLENGTH
        frequent_word_ms = -12.16  # WORDFREQUENCY
        sentence_position_ms = -0.23  # SENTENCEPOSITION

        if hasattr(self, "sentences"):
            total += sum(
                sentence_position_ms * sum(range(sentence.length))
                for sentence in self.sentences
            )
        else:
            total += sentence_position_ms * sum(range(self.length))

        total += len(self.words) * word_base_ms
        total += len(self.letters) * character_ms
        total += sum(
            frequent_word_ms * frequency
            for frequency in self.word_count.values()
            if frequency > 1
        )

        return total

    @filterabletextproperty
    def syllables(self):
        return sum(word.syllables for word in self.words)
