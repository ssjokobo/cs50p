import pytest
from fuel import convert, gauge


# test convert
def test_convert():

    # catching errors
    with pytest.raises(ValueError):
        assert convert("X/30")
    with pytest.raises(ValueError):
        assert convert("40/Y")
    with pytest.raises(ZeroDivisionError):
        assert convert("40/0")

    # catching calculations
    assert convert("4/8") == 50


# test gauge
def test_gauge():

    # E
    assert gauge(-1) == "E"
    assert gauge(0) == "E"
    assert gauge(0.5) == "E"
    assert gauge(1) == "E"

    # F
    assert gauge(99) == "F"
    assert gauge(105) == "F"

    # precentage
    assert gauge(25) == "25%"