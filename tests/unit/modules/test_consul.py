import pytest
import salt.modules.test as testmod
import saltext.consul.modules.consul_mod as consul_module


@pytest.fixture
def configure_loader_modules():
    module_globals = {
        "__salt__": {"test.echo": testmod.echo},
    }
    return {
        consul_module: module_globals,
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    assert consul_module.example_function(echo_str) == echo_str
