from jar import Jar
import pytest


def test_init():
    jar = Jar()

    # catching value after init
    assert jar.capacity == 12
    assert jar.size == 0


def test_str():
    jar = Jar()

    # catching cookies emoji string
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()

    # catching ValueError
    with pytest.raises(ValueError):
        assert jar.deposit(20)


def test_withdraw():
    jar = Jar()

    # catching ValueError
    with pytest.raises(ValueError):
        assert jar.withdraw(1)


def test_capacity():
    jar = Jar()

    # catching return
    assert jar.capacity == 12


def test_size():
    jar = Jar()

    # catching return
    assert jar.size == 0