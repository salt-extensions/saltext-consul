import pytest

pytestmark = [
    pytest.mark.requires_salt_states("consul.exampled"),
]


@pytest.fixture
def consul(states):
    return states.consul


def test_replace_this_this_with_something_meaningful(consul):
    echo_str = "Echoed!"
    ret = consul.exampled(echo_str)
    assert ret.result
    assert not ret.changes
    assert echo_str in ret.comment
