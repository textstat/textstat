"""Abstract base class for citation formatters."""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from textstat.citation.metadata import Citation


class CitationFormatter(ABC):
    """Abstract base class for citation formatters.

    Subclasses must implement format() and format_author() methods.
    Provides utility methods for common formatting tasks.
    """

    @abstractmethod
    def format(self, citation: "Citation") -> str:
        """Format a citation in this style.

        Args:
            citation: The citation metadata to format.

        Returns:
            Formatted citation string.
        """
        ...

    @abstractmethod
    def format_author(self, authors: list[str]) -> str:
        """Format author name(s) according to style.

        Args:
            authors: List of author names to format.

        Returns:
            Formatted author string.
        """
        ...

    def format_doi(self, doi: str) -> str:
        """Format DOI with standard prefix.

        Args:
            doi: Digital Object Identifier.

        Returns:
            Formatted DOI string.
        """
        if not doi.startswith("doi:") and not doi.startswith("https://doi.org/"):
            return f"doi:{doi}"
        return doi

    def format_pages(self, pages: str) -> str:
        """Format page range.

        Args:
            pages: Page range string.

        Returns:
            Formatted page range.
        """
        return pages
