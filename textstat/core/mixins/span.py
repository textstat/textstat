from __future__ import annotations

from typing import TYPE_CHECKING

from textstat.core.word import Word
from textstat.properties import Comparison, textproperty

if TYPE_CHECKING:  # pragma: no cover
    from ..sentence import Sentence


class Span:
    """A span can be a paragraph, a sentence, or a whole text.

    This mixin provides functionality for text spans that contain words,
    including the ability to extract words and filter them based on properties.
    """

    word_class = Word

    @textproperty
    def words(self) -> list[Word]:
        """A list of all words found in this span.

        Words are extracted using the word_class regex pattern.

        Returns:
            List of Word objects found in the text.
        """
        return [
            self.word_class(word) for word in self.word_class.regex.findall(self.text)
        ]

    def filter(self, comp: Comparison) -> list[Word | Sentence]:
        """Filter words or sentences based on a comparison condition.

        This method allows filtering using property comparisons, such as
        finding all words with 3 or more syllables or all sentences with
        specific lengths.

        Args:
            comp: A Comparison object created by using comparison operators
                on property objects (e.g., Word.syllables >= 3).

        Returns:
            List of Word or Sentence objects that match the comparison.

        Examples:
            >>> text.filter(Word.syllables >= 3)  # Words with 3+ syllables
            >>> text.filter(Word.length > 6)  # Words longer than 6 letters
            >>> text.filter(Sentence.length < 5)  # Short sentences
        """
        return [item for item in getattr(self, comp.type_name) if comp.compare(item)]

    def __iter__(self):
        return iter(self.words)
