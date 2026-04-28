from bank import value

def test_start_hello():
    assert value("hello") == 0

def test_start_h():
    assert value("hi") == 20

def test_start_other():
    assert value("good morning") == 100
    assert value("what's up") == 100