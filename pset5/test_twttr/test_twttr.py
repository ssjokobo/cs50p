from twttr import shorten


# test vowels, consonants, and mixed
def test_letter():
    assert shorten("aeiou") == ""
    assert shorten("bcdfg") == "bcdfg"
    assert shorten("abcde") == "bcd"


# test lower, upper, and mixed
def test_case():
    assert shorten("spoon") == "spn"
    assert shorten("SPOON") == "SPN"
    assert shorten("SpoOn") == "Spn"


# test numbers and symbols
def test_non_letter():
    assert shorten("12345") == "12345"
    assert shorten("!@&\"") == "!@&\""