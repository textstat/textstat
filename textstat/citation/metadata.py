"""Citation metadata dataclass."""

from dataclasses import asdict, dataclass, fields
from typing import Optional, Union


@dataclass
class JournalSource:
    """Represents a journal article source.

    Attributes:
        name: Journal name
        volume: Volume number (can be int or string)
        issue: Issue number (can be int or string)
        pages: Page range (e.g., "221-232")
    """

    name: Optional[str] = None
    volume: Optional[int | str] = None
    issue: Optional[int | str] = None
    pages: Optional[str] = None


@dataclass
class BookSource:
    """Represents a book source.

    Attributes:
        publisher: Publisher name
        isbn: ISBN number
        edition: Edition information
    """

    publisher: Optional[str] = None
    isbn: Optional[str] = None
    edition: Optional[str] = None


@dataclass
class WebSource:
    """Represents a web source.

    Attributes:
        url: Web URL
        accessed: Access date
    """

    url: Optional[str] = None
    accessed: Optional[str] = None


# Union type for all source types
Source = Union[JournalSource, BookSource, WebSource]


@dataclass
class Citation:
    """Represents citation metadata for a formula or method.

    Attributes:
        authors: List of author names in citation format (e.g., ["Flesch, R."])
        title: Full title of the work
        year: Publication year
        source: Source object (JournalSource, BookSource, or WebSource)
        doi: Digital Object Identifier
        notes: Additional notes
    """

    # Required fields
    authors: list[str]
    title: str
    year: int

    # Optional fields
    source: Optional[Source] = None
    doi: Optional[str] = None
    notes: Optional[str] = None

    def to_dict(self) -> dict:
        """Convert citation to dictionary representation.

        Returns:
            Dictionary with all non-None citation fields.
        """
        return {k: v for k, v in asdict(self).items() if v is not None}

    @classmethod
    def from_dict(cls, data: dict) -> "Citation":
        """Create Citation from dictionary.

        Args:
            data: Dictionary containing citation fields.

        Returns:
            Citation instance created from dictionary.
        """
        # Filter to only valid field names
        valid_fields = {f.name for f in fields(cls)}
        filtered_data = {k: v for k, v in data.items() if k in valid_fields}

        # Reconstruct source object if it exists as a dict
        if "source" in filtered_data and isinstance(filtered_data["source"], dict):
            source_dict = filtered_data["source"]
            # Determine which source type based on the keys present
            if (
                "name" in source_dict
                or "volume" in source_dict
                or "issue" in source_dict
                or "pages" in source_dict
            ):
                filtered_data["source"] = JournalSource(**source_dict)
            elif (
                "publisher" in source_dict
                or "isbn" in source_dict
                or "edition" in source_dict
            ):
                filtered_data["source"] = BookSource(**source_dict)
            elif "url" in source_dict or "accessed" in source_dict:
                filtered_data["source"] = WebSource(**source_dict)

        return cls(**filtered_data)
