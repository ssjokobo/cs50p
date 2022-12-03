from bank import value


# test hello
def test_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0


# test h
def test_h():
    assert value("hi") == 20
    assert value("Hi") == 20


# test others
def test_others():
    assert value("asdf") == 100
    assert value("1234") == 100
    assert value("@#$^") == 100