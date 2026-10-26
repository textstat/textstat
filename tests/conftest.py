"""Make the ``textstat`` package importable without an install.

Tries, in order: the checked-out repo root (``..``) and this workdir's
``../textstat-src`` clone. Only directories that actually contain the
``textstat`` package are added.

Note: the syllable-based tests also need the NLTK ``cmudict`` corpus
(``python -m nltk.downloader cmudict``), exactly like the upstream
suite does; nothing here downloads data.
"""

import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_CANDIDATES = (
    os.path.join(_HERE, ".."),
    os.path.join(_HERE, "..", "textstat-src"),
)
for _candidate in _CANDIDATES:
    if os.path.isdir(os.path.join(_candidate, "textstat")):
        sys.path.insert(0, os.path.normpath(_candidate))
