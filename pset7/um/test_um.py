from um import count


def test_count():

    # normal case
    assert count("Hello world") == 0
    assert count("Hello um") == 1
    assert count("um") == 1
    assert count("Um... um") == 2

    # words including um
    assert count("Umbrella") == 0
    assert count("Hello Prof. Umbridge") == 0
    assert count("That album is um...") == 1