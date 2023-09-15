from twttr import shorten

def test_consonants():
    assert shorten("rythm") == "rythm"

def test_vowels():
    assert shorten("noon") == "nn"

def test_nums():
    assert shorten("123") == "123"

def test_ucase():
    assert shorten("HELLO") == "HLL"

def test_lcase():
    assert shorten("hello") == "hll"

def test_punctuation():
    assert shorten("why??") == "why??"