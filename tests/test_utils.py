import pytest
from app.utils import retry


def test_retry_success():
    @retry(attempts=2, delay=0)
    def success():
        return True

    assert success() is True


def test_retry_failure():
    @retry(attempts=2, delay=0)
    def fail():
        raise Exception("Error")

    with pytest.raises(Exception):
        fail()
