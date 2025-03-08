from __future__ import annotations

from typing import Callable
import pytest
from textstat.backend import utils, counts, metrics
from .. import resources


@pytest.mark.parametrize(
    "inner_func, outer_funcs",
    [
        (
            counts.count_words,
            [metrics.sentences_per_word, metrics.words_per_sentence],
        ),
        (
            counts.count_letters,
            [metrics.letters_per_word, counts.count_letters, counts.count_letters],
        ),
    ],
)
def test_typed_chache(
    inner_func: Callable[[str], utils.constants.T],
    outer_funcs: list[Callable[[str], utils.constants.T]],
) -> None:
    # clear caches from other tests before running this one
    inner_func.cache_clear()  # type: ignore
    for outer_func in outer_funcs:
        outer_func.cache_clear()  # type: ignore

    # For simplicity just gonna test on some lang-less ones
    for outer_func in outer_funcs:
        outer_func(resources.SHORT_TEXT)

    assert inner_func.cache_info().misses == 1  # type: ignore
    assert inner_func.cache_info().hits == len(outer_funcs) - 1  # type: ignore

    inner_func(resources.SHORT_TEXT)

    assert inner_func.cache_info().misses == 1  # type: ignore
    assert inner_func.cache_info().hits == len(outer_funcs)  # type: ignore
