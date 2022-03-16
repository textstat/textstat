import pytest

from textstat import Stats


def test_stats_cant_be_instantiated():
    with pytest.raises(TypeError):
        Stats("")
