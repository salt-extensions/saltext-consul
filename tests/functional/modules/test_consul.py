import pytest

pytestmark = [
    pytest.mark.requires_salt_modules("consul.example_function"),
]


@pytest.fixture
def consul(modules):
    return modules.consul


def test_replace_this_this_with_something_meaningful(consul):
    echo_str = "Echoed!"
    res = consul.example_function(echo_str)
    assert res == echo_str
