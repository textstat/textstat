"""Tests for @citeable decorator and CitableMethod."""

import pytest
import inspect
from textstat.citation import citeable, Citation, CitableMethod
from textstat.citation.metadata import JournalSource


class TestCiteableDecorator:
    """Test the @citeable decorator."""

    def test_decorated_method_preserves_behavior(self):
        """Decorated method should work identically to undecorated method."""

        class TestClass:
            def __init__(self, value):
                self.value = value

            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return self.value * 2

        obj = TestClass(5)
        result = obj.test_method()
        assert result == 10

    def test_decorated_method_with_arguments(self):
        """Decorated method should handle arguments correctly."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self, a, b, c=10):
                return a + b + c

        obj = TestClass()
        assert obj.test_method(1, 2) == 13
        assert obj.test_method(1, 2, c=5) == 8

    def test_decorated_method_returns_correct_type(self):
        """Decorated method should preserve return type."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self) -> float:
                return 42.5

        obj = TestClass()
        result = obj.test_method()
        assert isinstance(result, float)
        assert result == 42.5

    def test_class_level_access_returns_citable_method(self):
        """Class-level access should return CitableMethod wrapper."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        method = TestClass.test_method
        assert isinstance(method, CitableMethod)

    def test_instance_level_access_returns_bound_method(self):
        """Instance-level access should return callable bound method."""

        class TestClass:
            def __init__(self, value):
                self.value = value

            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return self.value

        obj = TestClass(42)
        method = obj.test_method
        assert callable(method)
        assert method() == 42

    def test_decorated_method_preserves_name(self):
        """Decorated method should preserve __name__."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        assert TestClass.test_method.__name__ == "test_method"

    def test_decorated_method_preserves_docstring(self):
        """Decorated method should preserve __doc__."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                """This is a test method."""
                return 42

        assert TestClass.test_method.__doc__ == "This is a test method."

    def test_decorated_method_preserves_signature(self):
        """Decorated method should preserve signature for inspection."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self, a: int, b: str = "default") -> float:
                """Test method with signature."""
                return 42.0

        # Access the original function for signature inspection
        sig = inspect.signature(TestClass.test_method.func)
        params = list(sig.parameters.keys())
        assert "self" in params
        assert "a" in params
        assert "b" in params


class TestCitableMethod:
    """Test the CitableMethod wrapper class."""

    def test_citation_attribute_exists(self):
        """CitableMethod should have citation attribute."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        citation = TestClass.test_method.citation
        assert isinstance(citation, Citation)

    def test_citation_stores_metadata(self):
        """CitableMethod should store citation metadata correctly."""

        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, issue=3, pages="221-232"
        )

        class TestClass:
            @citeable(
                authors=["Flesch, R."],
                title="A new readability yardstick",
                year=1948,
                source=source,
                doi="10.1037/h0057532",
            )
            def test_method(self):
                return 42

        citation = TestClass.test_method.citation
        assert citation.authors == ["Flesch, R."]
        assert citation.title == "A new readability yardstick"
        assert citation.year == 1948
        assert citation.source.name == "Journal of Applied Psychology"
        assert citation.source.volume == 32
        assert citation.source.issue == 3
        assert citation.source.pages == "221-232"
        assert citation.doi == "10.1037/h0057532"

    def test_cite_method_exists(self):
        """CitableMethod should have cite() method."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        assert hasattr(TestClass.test_method, "cite")
        assert callable(TestClass.test_method.cite)

    def test_cite_method_returns_string(self):
        """cite() method should return a string."""

        source = JournalSource(
            name="Journal of Applied Psychology", volume=32, issue=3, pages="221-232"
        )

        class TestClass:
            @citeable(
                authors=["Flesch, R."],
                title="A new readability yardstick",
                year=1948,
                source=source,
                doi="10.1037/h0057532",
            )
            def test_method(self):
                return 42

        citation_string = TestClass.test_method.cite("harvard")
        assert isinstance(citation_string, str)
        assert len(citation_string) > 0

    def test_citation_styles_property_exists(self):
        """CitableMethod should have citation_styles property."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        assert hasattr(TestClass.test_method, "citation_styles")

    def test_citation_styles_returns_list(self):
        """citation_styles should return a list of style names."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        styles = TestClass.test_method.citation_styles
        assert isinstance(styles, list)
        assert len(styles) > 0
        assert all(isinstance(s, str) for s in styles)

    def test_citation_styles_includes_expected_styles(self):
        """citation_styles should include standard academic styles."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        styles = TestClass.test_method.citation_styles
        assert "harvard" in styles
        assert "apa" in styles
        assert "mla" in styles
        assert "chicago" in styles
        assert "bibtex" in styles

    def test_unknown_citation_style_raises_error(self):
        """cite() should raise ValueError for unknown style."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        with pytest.raises(ValueError, match="Unknown citation style"):
            TestClass.test_method.cite("invalid_style")

    def test_cite_error_message_shows_available_styles(self):
        """Error message should list available styles."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        with pytest.raises(ValueError) as exc_info:
            TestClass.test_method.cite("invalid_style")

        error_message = str(exc_info.value)
        assert "invalid_style" in error_message
        assert "Available" in error_message or "available" in error_message

    def test_decorated_method_is_callable_from_class(self):
        """CitableMethod should be callable (edge case)."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        # Should be able to call with explicit self
        obj = TestClass()
        result = TestClass.test_method(obj)
        assert result == 42

    def test_multiple_instances_share_citation(self):
        """Multiple instances should share the same citation metadata."""

        class TestClass:
            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return 42

        obj1 = TestClass()
        obj2 = TestClass()

        # Both should access the same citation
        citation1 = TestClass.test_method.citation
        citation2 = TestClass.test_method.citation
        assert citation1 is citation2

    def test_decorated_method_with_property(self):
        """Decorator should work alongside other descriptors."""

        class TestClass:
            def __init__(self):
                self._value = 10

            @property
            def value(self):
                return self._value

            @citeable(
                authors=["Flesch, R."], title="A new readability yardstick", year=1948
            )
            def test_method(self):
                return self.value * 2

        obj = TestClass()
        assert obj.test_method() == 20
