import json
from itertools import cycle
from unittest.mock import mock_open, patch

import pytest

from config import Config


@pytest.fixture
def config_data():
    data = {
        "layers": [
            {
                "name": "main",
                "color": "#e63946",
                "primary_keys": [
                    ["a", "b", "c", "a", "b", "c"],
                    ["a", "b", "c", "a", "b", "c"],
                    ["a", "b", "c", "a", "b", "c"],
                    ["a", "b", "c", "a", "b", "c"],
                    ["a", "b", "c", "a", "b", "c"],
                ],
                "secondary_keys": [
                    ["a", "b", "c", "a", "b", "c"],
                    ["a", "b", "c", "a", "b", "c"],
                    ["a", "b", "c", "a", "b", "c"],
                    ["a", "b", "c", "a", "b", "c"],
                    ["a", "b", "c", "a", "b", "c"],
                ],
            }
        ]
    }
    with patch("config.open", mock_open(read_data=json.dumps(data))) as m:
        yield m


def test_config(config_data):
    c = Config.read()
    assert isinstance(c, Config)
