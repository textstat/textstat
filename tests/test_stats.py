
import pytest

from textstat_core.stats import Stats


def test_stats_cant_be_instantiated():
    with pytest.raises(TypeError):
        Stats("")
