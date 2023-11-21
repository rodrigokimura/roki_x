import pytest

from manager import Command, Commands


@pytest.fixture
def commands():
    return Commands()


def test_commands_containment_test(commands: Commands):
    assert "layer_1_hold" in commands
    assert "not_layer" not in commands


def test_commands_get_valid_command(commands: Commands):
    r = commands.get("layer_1_hold")
    assert isinstance(r, Command)
    assert r.type_ == "hold"
    assert r.index == 1


def test_commands_get_invalid_command(commands: Commands):
    r = commands.get("noop")
    assert isinstance(r, Command)
    assert r.type_ is None
    assert r.index == 0
    r = commands.get("layer_1_invalid")
    assert isinstance(r, Command)
    assert r.type_ is None
    assert r.index == 1
