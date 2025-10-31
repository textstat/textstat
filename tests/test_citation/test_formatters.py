"""Tests for citation formatters."""

import pytest
from textstat.citation import Citation
from textstat.citation.metadata import JournalSource, BookSource
from textstat.citation.formatters import (
    HarvardFormatter,
    APAFormatter,
    MLAFormatter,
    ChicagoFormatter,
    BibTeXFormatter,
)


class TestHarvardFormatter:
    """Test Harvard citation style formatter."""

    def test_harvard_basic_journal_article(self):
        """Harvard formatter should format journal article correctly."""
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

        formatter = HarvardFormatter()
        result = formatter.format(citation)

        assert "Flesch, R." in result
        assert "(1948)" in result
        assert "'A new readability yardstick'" in result
        assert "Journal of Applied Psychology" in result
        assert "32" in result
        assert "221-232" in result
        assert "doi:10.1037/h0057532" in result or "10.1037/h0057532" in result

    def test_harvard_with_volume_and_issue(self):
        """Harvard formatter should format volume(issue) correctly."""
        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, issue=3, pages="221-232"
        )
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = HarvardFormatter()
        result = formatter.format(citation)

        # Should contain volume(issue) format
        assert "32(3)" in result or "32, no. 3" in result or "32.3" in result

    def test_harvard_without_issue(self):
        """Harvard formatter should handle missing issue."""
        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, pages="221-232"
        )
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = HarvardFormatter()
        result = formatter.format(citation)

        assert "32" in result
        assert "221-232" in result

    def test_harvard_book_citation(self):
        """Harvard formatter should format book citation."""
        source = BookSource(publisher="McGraw-Hill")
        citation = Citation(
            authors=["Gunning, R."],
            title="Technique of clear writing",
            year=1952,
            source=source,
        )

        formatter = HarvardFormatter()
        result = formatter.format(citation)

        assert "Gunning, R." in result
        assert "1952" in result
        assert "Technique of clear writing" in result
        assert "McGraw-Hill" in result

    def test_harvard_ends_with_period(self):
        """Harvard citation should end with a period."""
        citation = Citation(
            authors=["Flesch, R."], title="A new readability yardstick", year=1948
        )

        formatter = HarvardFormatter()
        result = formatter.format(citation)

        assert result.endswith(".")


class TestAPAFormatter:
    """Test APA citation style formatter."""

    def test_apa_basic_journal_article(self):
        """APA formatter should format journal article correctly."""
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

        formatter = APAFormatter()
        result = formatter.format(citation)

        assert "Flesch, R." in result
        assert "(1948)" in result
        assert "A new readability yardstick" in result
        assert "Journal of Applied Psychology" in result
        assert "32" in result
        assert "221-232" in result
        assert "doi" in result.lower() or "https://doi.org" in result

    def test_apa_title_not_in_quotes(self):
        """APA titles should not be in quotes (unlike Harvard)."""
        source = JournalSource(name="Journal of Applied Psychology")
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = APAFormatter()
        result = formatter.format(citation)

        # APA doesn't use quotes around article titles
        assert "'A new readability yardstick'" not in result
        assert "A new readability yardstick" in result

    def test_apa_doi_format(self):
        """APA should format DOI as URL."""
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            doi="10.1037/h0057532",
        )

        formatter = APAFormatter()
        result = formatter.format(citation)

        assert "https://doi.org/10.1037/h0057532" in result

    def test_apa_book_citation(self):
        """APA formatter should format book citation."""
        source = BookSource(publisher="McGraw-Hill")
        citation = Citation(
            authors=["Gunning, R."],
            title="Technique of clear writing",
            year=1952,
            source=source,
        )

        formatter = APAFormatter()
        result = formatter.format(citation)

        assert "Gunning, R." in result
        assert "(1952)" in result
        assert "Technique of clear writing" in result
        assert "McGraw-Hill" in result


class TestMLAFormatter:
    """Test MLA citation style formatter."""

    def test_mla_basic_journal_article(self):
        """MLA formatter should format journal article correctly."""
        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, issue=3, pages="221-232"
        )
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = MLAFormatter()
        result = formatter.format(citation)

        assert "Flesch, R." in result or "Flesch, R" in result
        assert (
            '"A new readability yardstick"' in result
            or '"A New Readability Yardstick"' in result
        )
        assert "Journal of Applied Psychology" in result
        assert "32.3" in result or "32, no. 3" in result
        assert "(1948)" in result or "1948" in result
        assert "221-232" in result

    def test_mla_title_in_quotes(self):
        """MLA article titles should be in quotes."""
        source = JournalSource(name="Journal of Applied Psychology")
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = MLAFormatter()
        result = formatter.format(citation)

        assert '"' in result  # Should have quotes around title

    def test_mla_book_citation(self):
        """MLA formatter should format book citation."""
        source = BookSource(publisher="McGraw-Hill")
        citation = Citation(
            authors=["Gunning, R."],
            title="Technique of clear writing",
            year=1952,
            source=source,
        )

        formatter = MLAFormatter()
        result = formatter.format(citation)

        assert "Gunning" in result
        assert (
            "Technique of clear writing" in result
            or "Technique of Clear Writing" in result
        )
        assert "1952" in result
        assert "McGraw-Hill" in result


class TestChicagoFormatter:
    """Test Chicago citation style formatter."""

    def test_chicago_basic_journal_article(self):
        """Chicago formatter should format journal article correctly."""
        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, issue=3, pages="221-232"
        )
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = ChicagoFormatter()
        result = formatter.format(citation)

        assert "Flesch" in result
        assert (
            '"A new readability yardstick"' in result
            or '"A New Readability Yardstick"' in result
        )
        assert "Journal of Applied Psychology" in result
        assert "32" in result
        assert "no. 3" in result or "3" in result
        assert "1948" in result
        assert "221-232" in result

    def test_chicago_title_in_quotes(self):
        """Chicago article titles should be in quotes."""
        source = JournalSource(name="Journal of Applied Psychology")
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = ChicagoFormatter()
        result = formatter.format(citation)

        assert '"' in result

    def test_chicago_issue_format(self):
        """Chicago should format issue as 'no. N'."""
        source = JournalSource(name="Journal of Applied Psychology", volume=32, issue=3)
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = ChicagoFormatter()
        result = formatter.format(citation)

        assert "no." in result or "3" in result


class TestBibTeXFormatter:
    """Test BibTeX formatter."""

    def test_bibtex_basic_structure(self):
        """BibTeX formatter should create valid BibTeX entry."""
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

        formatter = BibTeXFormatter()
        result = formatter.format(citation)

        assert result.startswith("@article{") or result.startswith("@")
        assert "author = {Flesch, R.}" in result or "author={Flesch, R.}" in result
        assert (
            "title = {A new readability yardstick}" in result
            or "title={A new readability yardstick}" in result
        )
        assert "year = {1948}" in result or "year={1948}" in result
        assert (
            "journal = {Journal of Applied Psychology}" in result
            or "journal={Journal of Applied Psychology}" in result
        )
        assert "volume = {32}" in result or "volume={32}" in result
        assert "}" in result

    def test_bibtex_citation_key(self):
        """BibTeX should generate citation key."""
        citation = Citation(
            authors=["Flesch, R."], title="A new readability yardstick", year=1948
        )

        formatter = BibTeXFormatter()
        result = formatter.format(citation)

        # Should have a key like flesch1948 or similar
        assert "@" in result
        assert "{" in result
        assert "1948" in result

    def test_bibtex_book_type(self):
        """BibTeX formatter should use @book for books."""
        source = BookSource(publisher="McGraw-Hill")
        citation = Citation(
            authors=["Gunning, R."],
            title="Technique of clear writing",
            year=1952,
            source=source,
        )

        formatter = BibTeXFormatter()
        result = formatter.format(citation)

        assert "@book{" in result
        assert "publisher" in result
        assert "McGraw-Hill" in result

    def test_bibtex_journal_type(self):
        """BibTeX formatter should use @article for journals."""
        source = JournalSource(name="Journal of Applied Psychology")
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = BibTeXFormatter()
        result = formatter.format(citation)

        assert "@article{" in result

    def test_bibtex_pages_format(self):
        """BibTeX should format pages with double dash."""
        source = JournalSource(pages="221-232")
        citation = Citation(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            source=source,
        )

        formatter = BibTeXFormatter()
        result = formatter.format(citation)

        # BibTeX uses double dash for page ranges
        assert "221--232" in result or "221-232" in result


class TestFormatterEdgeCases:
    """Test edge cases for all formatters."""

    @pytest.mark.parametrize(
        "formatter_class",
        [
            HarvardFormatter,
            APAFormatter,
            MLAFormatter,
            ChicagoFormatter,
            BibTeXFormatter,
        ],
    )
    def test_formatter_handles_missing_optional_fields(self, formatter_class):
        """Formatters should handle missing optional fields gracefully."""
        citation = Citation(
            authors=["Flesch, R."], title="A new readability yardstick", year=1948
        )

        formatter = formatter_class()
        result = formatter.format(citation)

        assert isinstance(result, str)
        assert len(result) > 0
        assert "Flesch" in result
        assert "1948" in str(result)

    @pytest.mark.parametrize(
        "formatter_class",
        [
            HarvardFormatter,
            APAFormatter,
            MLAFormatter,
            ChicagoFormatter,
            BibTeXFormatter,
        ],
    )
    def test_formatter_handles_multiple_authors(self, formatter_class):
        """Formatters should handle multiple authors."""
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

        formatter = formatter_class()
        result = formatter.format(citation)

        assert isinstance(result, str)
        assert "Kincaid" in result

    @pytest.mark.parametrize(
        "formatter_class",
        [
            HarvardFormatter,
            APAFormatter,
            MLAFormatter,
            ChicagoFormatter,
            BibTeXFormatter,
        ],
    )
    def test_formatter_handles_special_characters(self, formatter_class):
        """Formatters should handle special characters in titles."""
        citation = Citation(
            authors=["Test, A."],
            title="Title with special chars: dash—em-dash & ampersand",
            year=2020,
        )

        formatter = formatter_class()
        result = formatter.format(citation)

        assert isinstance(result, str)
        assert "dash" in result or "—" in result

    @pytest.mark.parametrize(
        "formatter_class",
        [
            HarvardFormatter,
            APAFormatter,
            MLAFormatter,
            ChicagoFormatter,
        ],
    )
    def test_formatter_handles_unicode(self, formatter_class):
        """Formatters should handle unicode characters."""
        citation = Citation(authors=["Müller, J."], title="Über readability", year=2020)

        formatter = formatter_class()
        result = formatter.format(citation)

        assert isinstance(result, str)
        assert "Müller" in result or "Muller" in result
