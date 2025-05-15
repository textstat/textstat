from __future__ import annotations

from textstat.en.word import Word
from textstat.properties import filterableproperty


class Span:
    word_class = Word

    @property
    def reading_time(self) -> float:
        """Demberg, Vera, and Frank Keller.
        "Data from eye-tracking corpora as evidence for theories of syntactic processing complexity."
        Cognition 109.2 (2008): 193-210.
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

    @filterableproperty
    def syllables(self):
        return sum(word.syllables for word in self.words)
