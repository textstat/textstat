"""APA citation style formatter."""

from typing import TYPE_CHECKING

from .base import CitationFormatter

if TYPE_CHECKING:
    from textstat.citation.metadata import Citation


class APAFormatter(CitationFormatter):
    """APA (7th edition) citation style formatter.

    Format: Author. (Year). Title. Journal, Volume(Issue), Pages. https://doi.org/DOI
    """

    def format(self, citation: "Citation") -> str:
        """Format citation in APA style.

        Args:
            citation: Citation metadata to format.

        Returns:
            Formatted APA citation string.
        """
        parts = []

        # Author. (Year).
        parts.append(f"{self.format_author(citation.authors)}. ({citation.year}).")

        # Title.
        parts.append(f"{citation.title}.")

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
                    journal_part += f", {citation.source.pages}"
                if journal_part:
                    parts.append(journal_part + ".")
            elif isinstance(citation.source, BookSource):
                if citation.source.publisher:
                    parts.append(f"{citation.source.publisher}.")

        # DOI as URL
        if citation.doi:
            doi_url = citation.doi
            if not doi_url.startswith("https://doi.org/"):
                doi_url = doi_url.replace("doi:", "").strip()
                doi_url = f"https://doi.org/{doi_url}"
            parts.append(doi_url)

        return " ".join(parts)

    def format_author(self, authors: list[str]) -> str:
        """Format author name(s) in APA style.

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
            return f"{authors[0]}, & {authors[1]}"
        # For 3+ authors, use "Author1, Author2, & Author3" (APA uses &)
        return ", ".join(authors[:-1]) + f", & {authors[-1]}"
