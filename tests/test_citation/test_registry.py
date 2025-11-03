"""Tests for citation formatter registry."""

import pytest

from textstat.citation import Citation
from textstat.citation.formatters import (
    CitationFormatter,
    get_formatter,
    list_formatters,
    register_formatter,
)


class TestFormatterRegistry:
    """Test the formatter registration system."""

    def test_list_formatters_returns_list(self):
        """list_formatters should return a list."""
        formatters = list_formatters()
        assert isinstance(formatters, list)

    def test_list_formatters_includes_standard_styles(self):
        """list_formatters should include standard academic styles."""
        formatters = list_formatters()
        assert "harvard" in formatters
        assert "apa" in formatters
        assert "mla" in formatters
        assert "chicago" in formatters
        assert "bibtex" in formatters

    def test_list_formatters_returns_sorted_list(self):
        """list_formatters should return alphabetically sorted list."""
        formatters = list_formatters()
        assert formatters == sorted(formatters)

    def test_get_formatter_returns_formatter_instance(self):
        """get_formatter should return a formatter instance."""
        formatter = get_formatter("harvard")
        assert isinstance(formatter, CitationFormatter)

    def test_get_formatter_case_insensitive(self):
        """get_formatter should be case insensitive."""
        formatter1 = get_formatter("harvard")
        formatter2 = get_formatter("Harvard")
        formatter3 = get_formatter("HARVARD")

        # All should return a formatter (might be same instance)
        assert isinstance(formatter1, CitationFormatter)
        assert isinstance(formatter2, CitationFormatter)
        assert isinstance(formatter3, CitationFormatter)

    def test_get_formatter_unknown_style_raises_error(self):
        """get_formatter should raise ValueError for unknown style."""
        with pytest.raises(ValueError, match="Unknown citation style"):
            get_formatter("nonexistent_style")

    def test_get_formatter_error_lists_available_styles(self):
        """Error message should list available styles."""
        with pytest.raises(ValueError) as exc_info:
            get_formatter("invalid")

        error_message = str(exc_info.value)
        assert "invalid" in error_message
        assert "harvard" in error_message or "Available" in error_message

    def test_register_formatter_adds_new_formatter(self):
        """register_formatter should add a new formatter to registry."""

        class CustomFormatter(CitationFormatter):
            def format(self, citation):
                return f"Custom: {citation.title}"

            def format_author(self, authors):
                return authors[0] if authors else ""

        custom = CustomFormatter()
        register_formatter("custom", custom)

        formatters = list_formatters()
        assert "custom" in formatters

    def test_registered_formatter_is_retrievable(self):
        """Registered formatter should be retrievable via get_formatter."""

        class CustomFormatter(CitationFormatter):
            def format(self, citation):
                return f"Custom: {citation.title}"

            def format_author(self, authors):
                return authors[0] if authors else ""

        custom = CustomFormatter()
        register_formatter("myformat", custom)

        retrieved = get_formatter("myformat")
        assert isinstance(retrieved, CustomFormatter)

    def test_registered_formatter_works_with_citation(self):
        """Registered formatter should format citations correctly."""

        class CustomFormatter(CitationFormatter):
            def format(self, citation):
                return f"{self.format_author(citation.authors)} - {citation.title} ({citation.year})"

            def format_author(self, authors):
                return authors[0] if authors else ""

        custom = CustomFormatter()
        register_formatter("testformat", custom)

        citation = Citation(authors=["Test, A."], title="Test Title", year=2020)

        formatter = get_formatter("testformat")
        result = formatter.format(citation)
        assert result == "Test, A. - Test Title (2020)"

    def test_register_formatter_case_insensitive(self):
        """Formatter names should be stored case-insensitively."""

        class CustomFormatter(CitationFormatter):
            def format(self, citation):
                return "test"

            def format_author(self, authors):
                return authors[0] if authors else ""

        custom = CustomFormatter()
        register_formatter("CamelCase", custom)

        # Should be retrievable with different casing
        formatter = get_formatter("camelcase")
        assert isinstance(formatter, CitationFormatter)

    def test_all_standard_formatters_registered(self):
        """All standard formatters should be pre-registered."""
        required_formatters = ["harvard", "apa", "mla", "chicago", "bibtex"]
        available_formatters = list_formatters()

        for required in required_formatters:
            assert required in available_formatters, (
                f"{required} formatter not registered"
            )

    def test_all_standard_formatters_instantiable(self):
        """All standard formatters should be instantiable and usable."""
        from textstat.citation.metadata import JournalSource

        standard_styles = ["harvard", "apa", "mla", "chicago", "bibtex"]
        source = JournalSource(name="Test Journal")
        citation = Citation(
            authors=["Test, A."], title="Test Title", year=2020, source=source
        )

        for style in standard_styles:
            formatter = get_formatter(style)
            result = formatter.format(citation)
            assert isinstance(result, str)
            assert len(result) > 0


class TestCitationFormatterABC:
    """Test the CitationFormatter abstract base class."""

    def test_citation_formatter_is_abstract(self):
        """CitationFormatter should not be directly instantiable."""
        with pytest.raises(TypeError):
            CitationFormatter()

    def test_citation_formatter_requires_format_method(self):
        """Subclass must implement format method."""

        class IncompleteFormatter(CitationFormatter):
            def format_author(self, authors):
                return authors[0] if authors else ""

        with pytest.raises(TypeError):
            IncompleteFormatter()

    def test_citation_formatter_requires_format_author_method(self):
        """Subclass must implement format_author method."""

        class IncompleteFormatter(CitationFormatter):
            def format(self, citation):
                return "test"

        with pytest.raises(TypeError):
            IncompleteFormatter()

    def test_complete_formatter_can_be_instantiated(self):
        """Complete implementation should be instantiable."""

        class CompleteFormatter(CitationFormatter):
            def format(self, citation):
                return f"{self.format_author(citation.authors)} ({citation.year})"

            def format_author(self, authors):
                return authors[0] if authors else ""

        formatter = CompleteFormatter()
        assert isinstance(formatter, CitationFormatter)

    def test_formatter_format_doi_method(self):
        """Base class should provide format_doi utility."""

        class TestFormatter(CitationFormatter):
            def format(self, citation):
                if citation.doi:
                    return self.format_doi(citation.doi)
                return ""

            def format_author(self, authors):
                return authors[0] if authors else ""

        formatter = TestFormatter()
        citation = Citation(
            authors=["Test, A."], title="Test", year=2020, doi="10.1234/test"
        )

        result = formatter.format(citation)
        assert "doi:10.1234/test" in result or "10.1234/test" in result

    def test_formatter_format_pages_method(self):
        """Base class should provide format_pages utility."""
        from textstat.citation.metadata import JournalSource

        class TestFormatter(CitationFormatter):
            def format(self, citation):
                if (
                    citation.source
                    and hasattr(citation.source, "pages")
                    and citation.source.pages
                ):
                    return self.format_pages(citation.source.pages)
                return ""

            def format_author(self, authors):
                return authors[0] if authors else ""

        formatter = TestFormatter()
        source = JournalSource(pages="123-456")
        citation = Citation(
            authors=["Test, A."], title="Test", year=2020, source=source
        )

        result = formatter.format(citation)
        assert "123" in result
        assert "456" in result
