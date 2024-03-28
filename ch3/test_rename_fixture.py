import pytest


@pytest.fixture(name="ultimate_answer")
def ultimate_answer_fixture():
    return 23


def test_everything(ultimate_answer):
    assert ultimate_answer == 23
