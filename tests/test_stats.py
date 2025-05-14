import pytest

from textstat.core.mixins import Stats


def test_stats_cant_be_instantiated():
    with pytest.raises(TypeError):
        Stats("")
