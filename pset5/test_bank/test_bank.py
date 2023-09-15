from bank import value

def test_hello():
    assert value("hello") == 0

def test_h():
    assert value("hi") == 20

def test_no_h():
   assert value("sup") == 100

def test_num():
   assert value("100") == 100

def test_Ucase():
    assert value("HELLO") == 0
