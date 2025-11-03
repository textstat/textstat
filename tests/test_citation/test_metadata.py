"""Tests for Citation metadata dataclass."""

import pytest

from textstat.citation import Citation
from textstat.citation.metadata import BookSource, JournalSource, WebSource


class TestCitationDataclass:
    """Test the Citation dataclass."""

    def test_citation_with_required_fields_only(self):
        """Citation should be created with only required fields."""
        citation = Citation(
            authors=["Flesch, R."], title="A new readability yardstick", year=1948
        )
        assert citation.authors == ["Flesch, R."]
        assert citation.title == "A new readability yardstick"
        assert citation.year == 1948

    def test_citation_with_all_fields(self):
        """Citation should store all provided fields."""
        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, issue=3, pages="221-232"
        )
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
            doi="10.1037/h0057532",
        )
        assert citation.authors == ["Flesch, R."]
        assert citation.title == "A new readability yardstick"
        assert citation.year == 1948
        assert citation.source.name == "Journal of Applied Psychology"
        assert citation.source.volume == 32
        assert citation.source.issue == 3
        assert citation.source.pages == "221-232"
        assert citation.doi == "10.1037/h0057532"

    def test_citation_with_book_fields(self):
        """Citation should handle book-specific fields."""
        source = BookSource(publisher="McGraw-Hill", isbn="978-0070252066")
        citation = Citation(
            authors=["Gunning, R."],
            title="Technique of clear writing",
            year=1952,
            source=source,
        )
        assert citation.source.publisher == "McGraw-Hill"
        assert citation.source.isbn == "978-0070252066"

    def test_citation_with_website_fields(self):
        """Citation should handle website-specific fields."""
        source = WebSource(url="https://example.com", accessed="2024-01-15")
        citation = Citation(
            authors=["McLaughlin, G.H."],
            title="SMOG Grading - A New Readability Formula",
            year=1969,
            source=source,
        )
        assert citation.source.url == "https://example.com"
        assert citation.source.accessed == "2024-01-15"

    def test_citation_to_dict(self):
        """Citation should convert to dictionary."""
        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, issue=3, pages="221-232"
        )
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
            doi="10.1037/h0057532",
        )
        result = citation.to_dict()

        assert isinstance(result, dict)
        assert result["authors"] == ["Flesch, R."]
        assert result["title"] == "A new readability yardstick"
        assert result["year"] == 1948
        assert "source" in result
        assert result["doi"] == "10.1037/h0057532"

    def test_citation_from_dict(self):
        """Citation should be created from dictionary."""
        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, issue=3, pages="221-232"
        )
        data = {
            "authors": ["Flesch, R."],
            "title": "A new readability yardstick",
            "year": 1948,
            "source": source,
            "doi": "10.1037/h0057532",
        }
        citation = Citation.from_dict(data)

        assert citation.authors == ["Flesch, R."]
        assert citation.title == "A new readability yardstick"
        assert citation.year == 1948
        assert citation.source.name == "Journal of Applied Psychology"

    def test_citation_round_trip(self):
        """Citation should survive dict round-trip conversion."""
        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, issue=3, pages="221-232"
        )
        original = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
            doi="10.1037/h0057532",
        )

        data = original.to_dict()
        restored = Citation.from_dict(data)

        assert restored.authors == original.authors
        assert restored.title == original.title
        assert restored.year == original.year
        assert restored.source.name == original.source.name
        assert restored.source.volume == original.source.volume

    def test_citation_without_source(self):
        """Citation should allow optional source field."""
        citation = Citation(
            authors=["Flesch, R."], title="A new readability yardstick", year=1948
        )
        assert citation.source is None

    def test_citation_with_multiple_authors_list(self):
        """Citation should handle multiple authors as a list."""
        citation = Citation(
            authors=[
                "Kincaid, J.P.",
                "Fishburne, R.P.",
                "Rogers, R.L.",
                "Chissom, B.S.",
            ],
            title="Derivation of new readability formulas",
            year=1975,
        )
        assert "Kincaid, J.P." in citation.authors
        assert "Fishburne, R.P." in citation.authors
        assert "Rogers, R.L." in citation.authors
        assert "Chissom, B.S." in citation.authors

    def test_citation_with_notes(self):
        """Citation should store optional notes."""
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            notes="This is the seminal work on readability",
        )
        assert citation.notes == "This is the seminal work on readability"

    def test_citation_missing_required_fields(self):
        """Citation should require authors, title, and year."""
        with pytest.raises(TypeError):
            Citation(title="A new readability yardstick", year=1948)

        with pytest.raises(TypeError):
            Citation(authors=["Flesch, R."], year=1948)

        with pytest.raises(TypeError):
            Citation(authors=["Flesch, R."], title="A new readability yardstick")

    def test_citation_volume_can_be_string_or_int(self):
        """Citation volume should accept both string and int."""
        source1 = JournalSource(name="Journal", volume=32)
        source2 = JournalSource(name="Journal", volume="32")
        citation1 = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source1,
        )
        citation2 = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source2,
        )
        assert citation1.source.volume == 32
        assert citation2.source.volume == "32"

    def test_citation_issue_can_be_string_or_int(self):
        """Citation issue should accept both string and int."""
        source1 = JournalSource(name="Journal", issue=3)
        source2 = JournalSource(name="Journal", issue="3")
        citation1 = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source1,
        )
        citation2 = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source2,
        )
        assert citation1.source.issue == 3
        assert citation2.source.issue == "3"
