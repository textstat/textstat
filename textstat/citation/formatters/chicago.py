"""Chicago citation style formatter."""

from typing import TYPE_CHECKING

from .base import CitationFormatter

if TYPE_CHECKING:
    from textstat.citation.metadata import Citation


class ChicagoFormatter(CitationFormatter):
    """Chicago Manual of Style (17th edition) citation formatter.

    Format: Author. "Title." Journal Volume, no. Issue (Year): Pages.
    """

    def format(self, citation: "Citation") -> str:
        """Format citation in Chicago style.

        Args:
            citation: Citation metadata to format.

        Returns:
            Formatted Chicago citation string.
        """
        parts = []

        # Author.
        author = self.format_author(citation.authors)
        if not author.endswith("."):
            author += "."
        parts.append(author)

        # "Title."
        title = self._format_title(citation.title)
        parts.append(f'"{title}"')

        # Source details
        if citation.source:
            from textstat.citation.metadata import BookSource, JournalSource

            if isinstance(citation.source, JournalSource):
                journal_part = citation.source.name or ""
                if citation.source.volume:
                    journal_part += f" {citation.source.volume}"
                    if citation.source.issue:
                        journal_part += f", no. {citation.source.issue}"
                if citation.year:
                    journal_part += f" ({citation.year})"
                if citation.source.pages:
                    journal_part += f": {citation.source.pages}"
                if journal_part:
                    parts.append(journal_part + ".")
            elif isinstance(citation.source, BookSource):
                if citation.source.publisher:
                    parts.append(f"{citation.source.publisher}, {citation.year}.")
        else:
            parts.append(f"{citation.year}.")

        return " ".join(parts)

    def format_author(self, authors: list[str]) -> str:
        """Format author name(s) in Chicago style.

        Args:
            authors: List of author names.

        Returns:
            Formatted author string.
        """
        if not authors:
            return ""
        if len(authors) == 1:
            return authors[0]
        if len(authors) == 2:
            return f"{authors[0]}, and {authors[1]}"
        # For 3+ authors, use "Author1, Author2, and Author3"
        return ", ".join(authors[:-1]) + f", and {authors[-1]}"

    def _format_title(self, title: str) -> str:
        """Format title for Chicago style.

        Args:
            title: Title string.

        Returns:
            Formatted title (capitalize first letter of major words).
        """
        words = title.split()
        minor_words = {
            "a",
            "an",
            "and",
            "as",
            "at",
            "but",
            "by",
            "for",
            "in",
            "of",
            "on",
            "or",
            "the",
            "to",
            "up",
            "via",
        }

        formatted_words = []
        for i, word in enumerate(words):
            if i == 0 or i == len(words) - 1 or word.lower() not in minor_words:
                formatted_words.append(word.capitalize())
            else:
                formatted_words.append(word.lower())

        return " ".join(formatted_words)
