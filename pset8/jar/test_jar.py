from jar import Jar
import pytest

def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(14, 4)
    assert jar.capacity == 14
    assert jar.size == 4


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(10)
    assert jar.size == 10
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8

    jar = Jar(15, 13)
    with pytest.raises(ValueError):
        jar.deposit(4)



def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(8)
    assert jar.size == 2

    jar = Jar(10, 9)
    with pytest.raises(ValueError):
        jar.withdraw(13)



def test_size():
    jar = Jar()
    assert jar.size == 0
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(5)
    assert jar.size == 5

    with pytest.raises(ValueError):
        jar = Jar(10, -1)



def test_capacity():
    jar = Jar(10)
    assert jar.capacity == 10

    jar = Jar()
    jar.capacity = 16
    assert jar.capacity == 16