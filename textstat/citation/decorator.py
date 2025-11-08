"""Decorator for adding citation metadata to methods."""

import functools
from typing import Any, Callable

from .formatters import get_formatter, list_formatters
from .metadata import Citation


class CitableMethod:
    """Wrapper for methods with citation metadata.

    This descriptor enables dual access patterns:
    - Instance access (text.method()): Returns bound method that works normally
    - Class access (Text.method): Returns CitableMethod for citation access

    Attributes:
        func: The original function being wrapped
        citation: Citation metadata for this method
    """

    def __init__(self, func: Callable, citation: Citation, is_property: bool = False):
        self.func = func
        self.citation = citation
        self.instance = None
        self.owner = None
        self._is_property = is_property

        functools.update_wrapper(self, func)

    def __repr__(self) -> str:
        """Return a string representation similar to functions/methods."""
        if self._is_property:
            return f"<citeable property {self.__qualname__} at {hex(id(self))}>"
        elif self.instance is not None:
            return f"<bound citeable method {self.__qualname__} of {self.instance!r}>"
        else:
            return f"<citeable function {self.__qualname__} at {hex(id(self))}>"

    def __get__(self, instance: Any, owner: type) -> Any:
        """Descriptor protocol: handle instance vs class access.

        args:
            instance: The instance accessing the method (None for class access).
            owner: The class that owns the method.

        Returns:
            For properties on instance access: the computed property value
            For methods on instance access: self (CitableMethod) bound to instance
            For class access: self (CitableMethod) for citation access
        """
        self.instance = instance
        self.owner = owner

        if instance is not None and self._is_property:
            return self.func(instance)
        return self

    def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """Call the wrapped function.

        Handles four cases:
        - Method called on instance: self.instance is set, inject it as first arg
        - Method called on class with explicit instance: pass args through
        - Method called on class without instance: error!
        - Standalone function: both are None, pass args directly
        """
        if self.instance is not None:
            # Called as a method on an instance (e.g., text.method())
            return self.func(self.instance, *args, **kwargs)
        elif self.owner is not None:
            # Called on class (e.g., Text.method(...))
            # Check if first arg is an instance - if so, it's an explicit unbound call
            if args and isinstance(args[0], self.owner):
                # Called with explicit instance (e.g., Text.method(instance))
                return self.func(*args, **kwargs)
            else:
                # Called without proper instance - this is an error
                raise TypeError(
                    f"{self.owner.__name__}.{self.func.__name__}() missing required "
                    f"positional argument: 'self' (must be called on an instance)"
                )
        else:
            # Called as a standalone function
            return self.func(*args, **kwargs)

    def cite(self, style: str = "harvard") -> str:
        """Generate citation in specified style.

        Args:
            style: Citation style name (e.g., "harvard", "apa", "mla").

        Returns:
            Formatted citation string.

        Raises:
            ValueError: If the citation style is unknown.

        Example:
            >>> Text.flesch_reading_ease.cite("harvard")
            "Flesch, R. (1948) 'A new readability yardstick'..."
        """
        return get_formatter(style).format(self.citation)

    @property
    def citation_styles(self) -> list[str]:
        """List available citation styles.

        Returns:
            Sorted list of available citation style names.

        Example:
            >>> Text.flesch_reading_ease.citation_styles
            ['apa', 'bibtex', 'chicago', 'harvard', 'mla']
        """
        return list_formatters()


def citeable(**metadata: Any) -> Callable[[Callable], CitableMethod]:
    """Decorator to add citation metadata to a method.

    This decorator wraps a method with citation information, allowing users to:
    1. Call the method normally from instances
    2. Access citation information from the class

    Args:
        **metadata: Citation metadata fields (authors, title, year, etc.)
            See Citation class for available fields.

    Returns:
        Decorator function that wraps the method.

    Raises:
        TypeError: If required citation fields are missing.

    Example:
        @citeable(
            authors=["Flesch, R."],
            title="A new readability yardstick",
            year=1948,
            journal="Journal of Applied Psychology",
            volume=32,
            issue=3,
            pages="221-232",
            doi="10.1037/h0057532"
        )
        def flesch_reading_ease(self) -> float:
            return (
                206.835
                - (1.015 * self.avg("words", per="sentences"))
                - (84.6 * self.avg("syllables", per="words"))
            )

    Usage:
        # Normal method call
        text = Text("Example text")
        score = text.flesch_reading_ease()  # Returns float

        # Citation access
        citation = Text.flesch_reading_ease.cite("harvard")  # Returns string
        metadata = Text.flesch_reading_ease.citation  # Returns Citation object
        styles = Text.flesch_reading_ease.citation_styles  # Returns list
    """

    def decorator(target: Callable | property) -> CitableMethod:
        """Inner decorator that creates CitableMethod wrapper.

        Args:
            func: The function to decorate.

        Returns:
            CitableMethod wrapper around the function.
        """
        if is_property := isinstance(target, property):
            target = target.fget

        if not callable(target):
            raise TypeError(f"Cannot decorate {type(target).__name__}: not callable")

        return CitableMethod(target, Citation(**metadata), is_property)

    return decorator
