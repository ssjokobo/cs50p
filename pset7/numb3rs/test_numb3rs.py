from numb3rs import validate


def test_validate():

    # true cases
    assert validate("0.0.0.0") == True
    assert validate("1.2.3.4") == True
    assert validate("11.22.33.44") == True
    assert validate("111.222.111.222") == True
    assert validate("255.255.255.255") == True

    # false cases
    assert validate("111.222.333.444") == False
    assert validate("11,22,33,44") == False
    assert validate("....") == False
    assert validate("-1.-2.-3.-4") == False
    assert validate("256.256.256.256") == False
    assert validate("a.b.c.d") == False