
import os
from pathlib import Path

import pytest
import toml


tests_location = os.path.dirname(os.path.realpath(__file__))


@pytest.fixture(
    params=Path(os.path.join(tests_location, "texts")).glob("*.toml")
)
def test_text(request):
    yield toml.load(request.param)
