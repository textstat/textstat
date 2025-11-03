"""BibTeX citation formatter."""

import re
from typing import TYPE_CHECKING

from .base import CitationFormatter

if TYPE_CHECKING:
    from textstat.citation.metadata import Citation


class BibTeXFormatter(CitationFormatter):
    """BibTeX citation format formatter.

    Generates BibTeX entries for bibliography management tools.
    """

    def format(self, citation: "Citation") -> str:
        """Format citation in BibTeX format.

        Args:
            citation: Citation metadata to format.

        Returns:
            Formatted BibTeX entry.
        """
        from textstat.citation.metadata import BookSource, JournalSource, WebSource

        # Determine entry type based on source
        entry_type = "article"  # default
        if citation.source:
            if isinstance(citation.source, BookSource):
                entry_type = "book"
            elif isinstance(citation.source, WebSource):
                entry_type = "misc"
            elif isinstance(citation.source, JournalSource):
                entry_type = "article"

        # Generate citation key
        key = self._generate_key(citation)

        # Build BibTeX entry
        lines = [f"@{entry_type}{{{key},"]

        # Add fields
        lines.append(f"  author = {{{self.format_author(citation.authors)}}},")
        lines.append(f"  title = {{{citation.title}}},")
        lines.append(f"  year = {{{citation.year}}},")

        # Add source-specific fields
        if citation.source:
            if isinstance(citation.source, JournalSource):
                if citation.source.name:
                    lines.append(f"  journal = {{{citation.source.name}}},")
                if citation.source.volume:
                    lines.append(f"  volume = {{{citation.source.volume}}},")
                if citation.source.issue:
                    lines.append(f"  number = {{{citation.source.issue}}},")
                if citation.source.pages:
                    # BibTeX uses -- for page ranges
                    pages = citation.source.pages.replace("-", "--")
                    lines.append(f"  pages = {{{pages}}},")
            elif isinstance(citation.source, BookSource):
                if citation.source.publisher:
                    lines.append(f"  publisher = {{{citation.source.publisher}}},")
                if citation.source.isbn:
                    lines.append(f"  isbn = {{{citation.source.isbn}}},")
            elif isinstance(citation.source, WebSource):
                if citation.source.url:
                    lines.append(f"  url = {{{citation.source.url}}},")

        if citation.doi:
            doi = citation.doi.replace("doi:", "").strip()
            lines.append(f"  doi = {{{doi}}},")

        # Remove trailing comma from last field
        if lines[-1].endswith(","):
            lines[-1] = lines[-1][:-1]

        lines.append("}")

        return "\n".join(lines)

    def format_author(self, authors: list[str]) -> str:
        """Format author name(s) for BibTeX.

        Args:
            authors: List of author names.

        Returns:
            Formatted author string for BibTeX.
        """
        # BibTeX uses "and" to separate authors
        return " and ".join(authors)

    def _generate_key(self, citation: "Citation") -> str:
        """Generate BibTeX citation key.

        Args:
            citation: Citation metadata.

        Returns:
            Citation key (e.g., "flesch1948").
        """
        # Extract last name from first author
        if citation.authors:
            author_part = citation.authors[0].split(",")[0].strip()
        else:
            author_part = "unknown"
        # Remove special characters and convert to lowercase
        author_part = re.sub(r"[^a-zA-Z]", "", author_part).lower()

        return f"{author_part}{citation.year}"
