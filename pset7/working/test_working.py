import pytest
from working import convert


def test_convert():

    # true cases
    assert convert("1 AM to 2 PM") == "01:00 to 14:00"
    assert convert("1:30 AM to 2:30 PM") == "01:30 to 14:30"

    # error cases
    # range
    with pytest.raises(ValueError):
        assert convert("21 AM to 1 PM")
    with pytest.raises(ValueError):
        assert convert("0 AM to 1 PM")
    with pytest.raises(ValueError):
        assert convert("99:99 AM to 99:00 PM")

    # lower
    with pytest.raises(ValueError):
        assert convert("1 am to 3 pm")

    # AM PM
    with pytest.raises(ValueError):
        assert convert("1 KM to 3 PM")

    # no "to"
    with pytest.raises(ValueError):
        assert convert("1 AM 3 PM")
    with pytest.raises(ValueError):
        assert convert("1 AM till 3 PM")