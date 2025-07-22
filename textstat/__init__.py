from .textstat import textstat
from . import backend


__version__ = (0, 7, 8)


for attribute in dir(textstat):
    if callable(getattr(textstat, attribute)):
        if not attribute.startswith("_"):
            globals()[attribute] = getattr(textstat, attribute)


__all__ = ["textstat", "backend"]
