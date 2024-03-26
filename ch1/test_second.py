def test_pass():
    x = (1, 2, 3)
    assert x == (1, 2, 3)


def test_fail():
    x = (1, 2, 3)
    assert x == (3, 2, 1)
