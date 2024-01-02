import pytest
import salt.modules.test as testmod
import saltext.consul.modules.consul_mod as consul_module
import saltext.consul.states.consul_mod as consul_state


@pytest.fixture
def configure_loader_modules():
    return {
        consul_module: {
            "__salt__": {
                "test.echo": testmod.echo,
            },
        },
        consul_state: {
            "__salt__": {
                "consul.example_function": consul_module.example_function,
            },
        },
    }


def test_replace_this_this_with_something_meaningful():
    echo_str = "Echoed!"
    expected = {
        "name": echo_str,
        "changes": {},
        "result": True,
        "comment": f"The 'consul.example_function' returned: '{echo_str}'",
    }
    assert consul_state.exampled(echo_str) == expected
