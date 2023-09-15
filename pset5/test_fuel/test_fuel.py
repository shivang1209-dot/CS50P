import pytest
from fuel import convert, gauge


def test_val_error():
    with pytest.raises(ValueError):
        convert("x/y")

def test_zero_div_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("2/3") == 67
    assert convert("10/100") == 10

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
