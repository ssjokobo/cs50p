from project import swipe_left, swipe_right, swipe_up, swipe_down


table_a = [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
table_b = [[2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4], [2, 2, 4, 4]]
table_c = [[0, 0, 0, 0], [0, 2, 2, 0], [0, 2, 2, 0], [0, 0, 0, 0]]
table_d = [[8, 4, 2, 4], [16, 8, 4, 2], [64, 16, 2, 8], [256, 32, 16, 4]]


def test_swipe_left():
    assert swipe_left(table_a) == [[2, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 0]]
    assert swipe_left(table_b) == [[4, 8, 0, 0], [4, 8, 0, 0], [4, 8, 0, 0], [4, 8, 0, 0]]
    assert swipe_left(table_c) == [[0, 0, 0, 0], [4, 0, 0, 0], [4, 0, 0, 0], [0, 0, 0, 0]]
    assert swipe_left(table_d) == [[8, 4, 2, 4], [16, 8, 4, 2], [64, 16, 2, 8], [256, 32, 16, 4]]

def test_swipe_right():
    assert swipe_right(table_a) == [[0, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2]]
    assert swipe_right(table_b) == [[0, 0, 4, 8], [0, 0, 4, 8], [0, 0, 4, 8], [0, 0, 4, 8]]
    assert swipe_right(table_c) == [[0, 0, 0, 0], [0, 0, 0, 4], [0, 0, 0, 4], [0, 0, 0, 0]]
    assert swipe_right(table_d) == [[8, 4, 2, 4], [16, 8, 4, 2], [64, 16, 2, 8], [256, 32, 16, 4]]


def test_swipe_up():
    assert swipe_up(table_a) == [[2, 0, 0, 2], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert swipe_up(table_b) == [[4, 4, 8, 8], [4, 4, 8, 8], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert swipe_up(table_c) == [[0, 4, 4, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert swipe_up(table_d) == [[8, 4, 2, 4], [16, 8, 4, 2], [64, 16, 2, 8], [256, 32, 16, 4]]


def test_swipe_down():
    assert swipe_down(table_a) == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [2, 0, 0, 2]]
    assert swipe_down(table_b) == [[0, 0, 0, 0], [0, 0, 0, 0], [4, 4, 8, 8], [4, 4, 8, 8]]
    assert swipe_down(table_c) == [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 4, 4, 0]]
    assert swipe_down(table_d) == [[8, 4, 2, 4], [16, 8, 4, 2], [64, 16, 2, 8], [256, 32, 16, 4]]