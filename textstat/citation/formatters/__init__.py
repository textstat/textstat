"""Citation formatter registry and base classes."""

from .apa import APAFormatter
from .base import CitationFormatter
from .bibtex import BibTeXFormatter
from .chicago import ChicagoFormatter
from .harvard import HarvardFormatter
from .mla import MLAFormatter

# Global formatter registry
_FORMATTERS: dict[str, CitationFormatter] = {}


def register_formatter(name: str, formatter: CitationFormatter) -> None:
    """Register a citation formatter.

    Args:
        name: Name of the citation style (e.g., "harvard", "apa").
        formatter: CitationFormatter instance.
    """
    _FORMATTERS[name.lower()] = formatter


def get_formatter(name: str) -> CitationFormatter:
    """Get a formatter by name.

    Args:
        name: Name of the citation style.

    Returns:
        CitationFormatter instance.

    Raises:
        ValueError: If the citation style is not found.
    """
    name_lower = name.lower()
    if name_lower not in _FORMATTERS:
        available = ", ".join(sorted(_FORMATTERS.keys()))
        raise ValueError(
            f"Unknown citation style: {name}. Available styles: {available}"
        )
    return _FORMATTERS[name_lower]


def list_formatters() -> list[str]:
    """List all registered formatter names.

    Returns:
        Sorted list of registered formatter names.
    """
    return sorted(_FORMATTERS.keys())


# Register built-in formatters
register_formatter("harvard", HarvardFormatter())
register_formatter("apa", APAFormatter())
register_formatter("mla", MLAFormatter())
register_formatter("chicago", ChicagoFormatter())
register_formatter("bibtex", BibTeXFormatter())

__all__ = [
    "CitationFormatter",
    "HarvardFormatter",
    "APAFormatter",
    "MLAFormatter",
    "ChicagoFormatter",
    "BibTeXFormatter",
    "register_formatter",
    "get_formatter",
    "list_formatters",
]
