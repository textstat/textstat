from .textstat import textstat


__version__ = (0, 7, 2)


for attribute in dir(textstat):
    if callable(getattr(textstat, attribute)):
        if not attribute.startswith("_"):
            globals()[attribute] = getattr(textstat, attribute)



#
# Provide a second API that's PEP-8 and type-checker friendly.
#

from .textstat import analyzer_instance, TextStatistics

analyzer: TextStatistics = analyzer_instance
