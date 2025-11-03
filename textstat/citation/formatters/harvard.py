"""Harvard citation style formatter."""

from typing import TYPE_CHECKING

from .base import CitationFormatter

if TYPE_CHECKING:
    from textstat.citation.metadata import Citation


class HarvardFormatter(CitationFormatter):
    """Harvard (author-date) citation style formatter.

    Format: Author (Year) 'Title', Journal, Volume(Issue), pp. Pages. doi:DOI.
    """

    def format(self, citation: "Citation") -> str:
        """Format citation in Harvard style.

        Args:
            citation: Citation metadata to format.

        Returns:
            Formatted Harvard citation string.
        """
        parts = []

        # Author (Year)
        parts.append(f"{self.format_author(citation.authors)} ({citation.year})")

        # 'Title'
        parts.append(f"'{citation.title}'")

        # Source details
        if citation.source:
            from textstat.citation.metadata import BookSource, JournalSource

            if isinstance(citation.source, JournalSource):
                journal_part = citation.source.name or ""
                if citation.source.volume:
                    journal_part += f", {citation.source.volume}"
                    if citation.source.issue:
                        journal_part += f"({citation.source.issue})"
                if citation.source.pages:
                    journal_part += f", pp. {citation.source.pages}"
                if journal_part:
                    parts.append(journal_part)
            elif isinstance(citation.source, BookSource):
                if citation.source.publisher:
                    parts.append(citation.source.publisher)

        # DOI
        if citation.doi:
            parts.append(self.format_doi(citation.doi))

        return ". ".join(parts) + "."

    def format_author(self, authors: list[str]) -> str:
        """Format author name(s) in Harvard style.

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
            return f"{authors[0]} and {authors[1]}"
        # For 3+ authors, use "Author1, Author2, and Author3"
        return ", ".join(authors[:-1]) + f", and {authors[-1]}"
