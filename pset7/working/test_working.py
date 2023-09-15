from working import convert

def test_correct1():
    assert convert("9 AM To 5 PM") == "09:00 to 17:00"
def test_correct2():
    assert convert("9 AM To 5:30 PM") == "09:00 to 17:30"
def test_correct3():
    assert convert("9:30 AM to 4:00 PM") == "09:30 to 16:00"