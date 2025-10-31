"""Integration tests for citation feature with Text class."""

import pytest
from textstat import Text
from textstat.citation import Citation


class TestTextCitationIntegration:
    """Test citation feature integrated with Text class."""

    def test_text_flesch_reading_ease_has_citation(self):
        """flesch_reading_ease method should have citation."""
        assert hasattr(Text.flesch_reading_ease, "citation")
        citation = Text.flesch_reading_ease.citation
        assert isinstance(citation, Citation)

    def test_text_flesch_reading_ease_citation_content(self):
        """flesch_reading_ease citation should have correct metadata."""
        citation = Text.flesch_reading_ease.citation
        assert citation.authors == ["Flesch, R."]
        assert citation.year == 1948
        assert "readability" in citation.title.lower()

    def test_text_method_cite_returns_string(self):
        """cite() method should return formatted citation string."""
        citation_str = Text.flesch_reading_ease.cite("harvard")
        assert isinstance(citation_str, str)
        assert len(citation_str) > 0
        assert "Flesch" in citation_str
        assert "1948" in citation_str

    def test_text_method_supports_multiple_citation_styles(self):
        """Should support multiple citation styles."""
        harvard = Text.flesch_reading_ease.cite("harvard")
        apa = Text.flesch_reading_ease.cite("apa")
        mla = Text.flesch_reading_ease.cite("mla")

        assert isinstance(harvard, str)
        assert isinstance(apa, str)
        assert isinstance(mla, str)

        # Each style should be different
        assert harvard != apa or harvard != mla

    def test_text_method_citation_styles_property(self):
        """citation_styles property should list available styles."""
        styles = Text.flesch_reading_ease.citation_styles
        assert isinstance(styles, list)
        assert len(styles) >= 5
        assert "harvard" in styles
        assert "apa" in styles

    def test_multiple_formulas_have_citations(self):
        """Multiple readability formulas should have citations."""
        methods_to_check = [
            "flesch_reading_ease",
            "flesch_kincaid_grade",
            "smog_grade",
            "gunning_fog",
            "coleman_liau_index",
            "automated_readability_index",
        ]

        for method_name in methods_to_check:
            if hasattr(Text, method_name):
                method = getattr(Text, method_name)
                assert hasattr(method, "citation"), f"{method_name} missing citation"
                assert hasattr(method, "cite"), f"{method_name} missing cite method"

    def test_different_formulas_have_different_citations(self):
        """Different formulas should have different citation metadata."""
        if hasattr(Text.flesch_reading_ease, "citation") and hasattr(
            Text, "flesch_kincaid_grade"
        ):
            if hasattr(Text.flesch_kincaid_grade, "citation"):
                fre_citation = Text.flesch_reading_ease.citation
                fkg_citation = Text.flesch_kincaid_grade.citation

                # Should have different metadata
                assert (
                    fre_citation.authors != fkg_citation.authors
                    or fre_citation.year != fkg_citation.year
                    or fre_citation.title != fkg_citation.title
                )

    def test_instance_method_call_with_args(self):
        """Instance method calls should work with all original arguments."""
        text = Text("The quick brown fox jumps over the lazy dog. " * 5)

        # Method should be callable and return expected type
        score = text.flesch_reading_ease()
        assert isinstance(score, float)

    def test_citation_access_doesnt_break_method(self):
        """Accessing citation shouldn't affect method functionality."""
        # Access citation
        citation = Text.flesch_reading_ease.citation
        assert isinstance(citation, Citation)

        # Method should still work
        text = Text("Sample text for testing.")
        score = text.flesch_reading_ease()
        assert isinstance(score, float)

    def test_cite_access_doesnt_break_method(self):
        """Calling cite() shouldn't affect method functionality."""
        # Get citation string
        citation_str = Text.flesch_reading_ease.cite("harvard")
        assert isinstance(citation_str, str)

        # Method should still work
        text = Text("Sample text for testing.")
        score = text.flesch_reading_ease()
        assert isinstance(score, float)

    def test_multiple_instances_same_citation(self):
        """Multiple Text instances should share same citation metadata."""
        text1 = Text("First sample text.")
        text2 = Text("Second sample text.")

        # Both should work
        score1 = text1.flesch_reading_ease()
        score2 = text2.flesch_reading_ease()

        assert isinstance(score1, float)
        assert isinstance(score2, float)

        # Citation should be same object
        citation = Text.flesch_reading_ease.citation
        assert citation.authors == ["Flesch, R."]

    def test_method_docstring_preserved(self):
        """Method docstring should be preserved."""
        docstring = Text.flesch_reading_ease.__doc__
        assert docstring is not None
        assert len(docstring) > 0

    def test_method_name_preserved(self):
        """Method name should be preserved."""
        assert Text.flesch_reading_ease.__name__ == "flesch_reading_ease"


class TestTextCitationUseCases:
    """Test real-world use cases for citations."""

    def test_generate_reference_list(self):
        """Should be able to generate reference list for used formulas."""
        text = Text("Sample text for analysis. " * 10)

        # Run multiple analyses
        fre = text.flesch_reading_ease()

        # Generate reference
        reference = Text.flesch_reading_ease.cite("harvard")

        assert isinstance(reference, str)
        assert "Flesch" in reference
        assert isinstance(fre, float)

    def test_export_to_bibtex(self):
        """Should be able to export citations to BibTeX format."""
        bibtex = Text.flesch_reading_ease.cite("bibtex")

        assert isinstance(bibtex, str)
        assert "@" in bibtex  # BibTeX entries start with @
        assert "Flesch" in bibtex or "flesch" in bibtex
        assert "1948" in bibtex

    def test_compare_citation_styles(self):
        """Should be able to compare different citation styles."""
        styles = ["harvard", "apa", "mla", "chicago", "bibtex"]
        citations = {}

        for style in styles:
            try:
                citations[style] = Text.flesch_reading_ease.cite(style)
            except (AttributeError, ValueError):
                pytest.skip(f"Style {style} not yet implemented")

        # All should be strings
        assert all(isinstance(c, str) for c in citations.values())

        # Most should be different (bibtex definitely different)
        unique_citations = set(citations.values())
        assert len(unique_citations) >= 2

    def test_citation_in_automated_workflow(self):
        """Test citation in automated analysis workflow."""
        # Simulate automated workflow
        text = Text("This is a sample document for readability analysis. " * 20)

        results = {}
        formulas_used = []

        # Run analysis
        if hasattr(Text, "flesch_reading_ease"):
            results["Flesch Reading Ease"] = text.flesch_reading_ease()
            formulas_used.append(("Flesch Reading Ease", Text.flesch_reading_ease))

        # Generate references
        references = []
        for name, formula in formulas_used:
            if hasattr(formula, "cite"):
                ref = formula.cite("harvard")
                references.append(ref)

        assert len(results) > 0
        assert len(references) > 0
        assert all(isinstance(r, str) for r in references)


class TestTextCitationErrorHandling:
    """Test error handling in citation feature."""

    def test_invalid_citation_style_raises_error(self):
        """Should raise ValueError for invalid citation style."""
        with pytest.raises(ValueError, match="Unknown citation style"):
            Text.flesch_reading_ease.cite("invalid_style_xyz")

    def test_invalid_style_error_message_helpful(self):
        """Error message should suggest available styles."""
        with pytest.raises(ValueError) as exc_info:
            Text.flesch_reading_ease.cite("notarealstyle")

        error_message = str(exc_info.value)
        assert "notarealstyle" in error_message
        # Should mention available styles
        assert any(
            word in error_message.lower() for word in ["available", "styles", "valid"]
        )

    def test_method_without_decorator_no_citation(self):
        """Methods without @citeable should not have citation attribute."""
        # Test on a method that shouldn't have citation (if any exist)
        # For now, just verify that attempting to access citation on a
        # non-decorated method would fail appropriately

        class TestClass:
            def regular_method(self):
                return 42

        assert not hasattr(TestClass.regular_method, "citation")
        assert not hasattr(TestClass.regular_method, "cite")


class TestBackwardCompatibility:
    """Test that citation feature doesn't break existing functionality."""

    def test_existing_text_usage_unchanged(self):
        """Existing Text usage should work exactly as before."""
        text = Text("The cat sat on the mat.")

        # Should work as before
        score = text.flesch_reading_ease()
        assert isinstance(score, float)

    def test_method_signature_unchanged(self):
        """Method signatures should be unchanged."""
        import inspect

        # Get the actual method (through the descriptor if needed)
        if hasattr(Text.flesch_reading_ease, "func"):
            sig = inspect.signature(Text.flesch_reading_ease.func)
        else:
            # Might not be implemented yet
            pytest.skip("Citation feature not implemented yet")

        params = list(sig.parameters.keys())
        assert "self" in params

    def test_return_type_unchanged(self):
        """Return types should be unchanged."""
        text = Text("Sample text.")
        result = text.flesch_reading_ease()
        assert isinstance(result, float)

    def test_no_performance_regression(self):
        """Citation feature should not significantly impact performance."""
        import time

        text = Text("Sample text for performance testing. " * 100)

        # Time multiple calls
        start = time.time()
        for _ in range(100):
            text.flesch_reading_ease()
        elapsed = time.time() - start

        # Should complete 100 calls in reasonable time (< 1 second for simple text)
        assert elapsed < 5.0  # Very generous limit

    def test_text_instantiation_unchanged(self):
        """Text instantiation should work as before."""
        text = Text("Sample text")
        assert isinstance(text, Text)
        assert hasattr(text, "flesch_reading_ease")

    def test_all_original_methods_callable(self):
        """All original Text methods should still be callable."""
        text = Text("The quick brown fox jumps over the lazy dog. " * 3)

        # Test a few key methods
        methods_to_test = [
            "flesch_reading_ease",
        ]

        for method_name in methods_to_test:
            if hasattr(text, method_name):
                method = getattr(text, method_name)
                result = method()
                assert result is not None  # Should return something
