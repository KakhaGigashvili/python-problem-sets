from twttr import no_vowels

def test_twitter():
    assert no_vowels("Twitter") == "Twttr"

def test_name():
    assert no_vowels("What's your name?") == "Wht's yr nm?"

def test_cs():
    assert no_vowels("CS50") == "CS50"