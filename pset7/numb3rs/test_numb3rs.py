from numb3rs import validate

def test_max():
    assert validate("255.255.255.255") == True

def test_myip():
    assert validate("255.255.0.17") == True

def test_string():
    assert validate("cat") == False

def test_overflow():
    assert validate("275.12.24.56") == False

def test_overflow2():
    assert validate("255.256.24.56") == False