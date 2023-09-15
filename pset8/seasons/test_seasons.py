import pytest
from seasons import valid_date


def main():
    test_valid_date()


def test_valid_date():
    assert valid_date("January 1, 1990") == None
    assert valid_date("1990-1-1") == None
    assert valid_date("1990-01-01") == ("1990", "01", "01")


if __name__ == "__main__":
    main()