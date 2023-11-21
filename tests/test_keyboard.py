from unittest.mock import MagicMock

import pytest

from kb import RokiX


class AsyncMock(MagicMock):
    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


def test_keyboard(config_data: MagicMock):
    r = RokiX(1)
    assert isinstance(r, RokiX)
    config_data.assert_called_once()
    assert r.layer == r.config.layers[0]


@pytest.mark.xfail()
@pytest.mark.asyncio
@pytest.mark.timeout(3)
async def test_keyboard_as_primary(config_data: MagicMock):
    r = RokiX(1)
    config_data.assert_called_once()
    await r.run()


@pytest.mark.xfail()
@pytest.mark.asyncio
@pytest.mark.timeout(3)
async def test_keyboard_as_secondary(config_data: MagicMock):
    r = RokiX(1)
    r._primary = False
    config_data.assert_called_once()
    await r.run()
