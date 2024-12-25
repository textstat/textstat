from __future__ import annotations

import pytest
from textstat.backend import utils


@pytest.mark.parametrize(
    "lang, n_words",
    [
        ("en", 2941),
        ("es", 20000),
        ("de", 2941),
        ("fr", 2941),
    ],
)
def test_get_lang_easy_words(lang: str, n_words: int) -> None:
    if lang not in ["en", "es"]:
        with pytest.warns(Warning):
            assert len(utils.get_lang_easy_words(lang)) == n_words
    else:
        assert len(utils.get_lang_easy_words(lang)) == n_words
