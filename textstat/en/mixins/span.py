from __future__ import annotations

from textstat.en.word import Word
from textstat.properties import filterableproperty


class Span:
    """English-specific span mixin providing reading time and syllable counting.

    This mixin extends the base Span class with English-specific properties
    such as estimated reading time and syllable counts.
    """

    word_class = Word

    @property
    def reading_time(self) -> float:
        """Estimate the reading time in milliseconds.

        Uses a regression model based on eye-tracking data to estimate
        how long it would take to read this text. The model accounts for:
        - Base time per word (275ms)
        - Character length effects (14.69ms per character)
        - Word frequency effects (-12.16ms for repeated words)
        - Sentence position effects (-0.23ms per position)

        Reference:
            Demberg, Vera, and Frank Keller.
            "Data from eye-tracking corpora as evidence for theories of
            syntactic processing complexity."
            Cognition 109.2 (2008): 193-210.

        Returns:
            Estimated reading time in milliseconds.

        Examples:
            >>> text = Text("This is a sample sentence.")
            >>> text.reading_time  # Returns time in milliseconds
            1523.45
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
        """The total number of syllables in all words.

        Sums the syllable counts from all words in this span.
        Syllable counting uses CMU Pronouncing Dictionary when available,
        falling back to algorithmic estimation.

        Returns:
            Total count of syllables.

        Examples:
            >>> text = Text("Hello world")
            >>> text.syllables
            3
        """
        return sum(word.syllables for word in self.words)
