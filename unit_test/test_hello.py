from hello import hello

def test_hello():
    assert hello() == "hello, word"

def test_argument():
    assert hello("Alice") == "hello, Alice"
