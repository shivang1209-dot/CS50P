import pytest
from project import validate_input,assign_house,calculate_age

def test_validate_input():
    with pytest.raises(SystemExit):
        validate_input()

def test_assign_house():
    assert assign_house("Rohit") in ["Gryffindor, Ravenclaw,","Hufflepuff","Slytherin"]

def test_calculate_age():
    assert calculate_age(2004) == 19
    assert calculate_age(2003) == 20
    assert calculate_age(2002) == 21
    assert calculate_age(2005) == 18