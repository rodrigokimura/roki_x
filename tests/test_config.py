from unittest.mock import MagicMock

from firmware.config import Config


def test_config(config_data: MagicMock):
    c = Config.read()
    assert isinstance(c, Config)
    config_data.assert_called_once()
    assert c.layer == c.layers[0]
