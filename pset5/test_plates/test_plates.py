from plates import is_valid


# non-alnum
def test_alnum():
    assert is_valid("AAA#$1") == False


# length 2-6 chars
def test_length():
    assert is_valid("") == False
    assert is_valid("A") == False
    assert is_valid("AAA1233") == False


# first two are alphabet
def test_first_two():
    assert is_valid("1A") == False
    assert is_valid("112342") == False
    assert is_valid("A1ALKF") == False


# commit to number after appear after first two
def test_():
    assert is_valid("AS123A") == False
    assert is_valid("AA1S1S") == False


# first number is zero
def test_first_num_zero():
    assert is_valid("ASD098") == False
    assert is_valid("AS0872") == False


# correct case
def test_correct():
    assert is_valid("AA") == True
    assert is_valid("AA1093") == True
    assert is_valid("AABBCC") == True
    assert is_valid("AAA111") == True