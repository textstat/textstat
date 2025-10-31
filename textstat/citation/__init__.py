"""Citation system for textstat formulas.

This package provides decorators and utilities to attach citation metadata
to readability formulas, enabling automatic generation of properly formatted
citations in various academic styles.

Example:
    from textstat import Text
    
    # Get citation in Harvard style
    citation = Text.flesch_reading_ease.cite("harvard")
    
    # Get citation metadata
    metadata = Text.flesch_reading_ease.citation
    
    # List available citation styles
    styles = Text.flesch_reading_ease.citation_styles
"""

from .metadata import Citation
from .decorator import citeable, CitableMethod
from .formatters import CitationFormatter, register_formatter, list_formatters

__all__ = [
    "Citation",
    "citeable",
    "CitableMethod",
    "CitationFormatter",
    "register_formatter",
    "list_formatters",
]

