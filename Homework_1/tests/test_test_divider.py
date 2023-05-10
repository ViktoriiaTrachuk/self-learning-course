import pytest
from test_src.test_divider import divide

@pytest.mark.parametrize("x,y,expected", [
    (10, 2, 5),
    (-10, 2, -5),
    (10, -2, -5),
    (-10, -2, 5),
    (10.0, 2.0, 5.0),
    (-6.0, -2.0, 3.0),
    (4.0, -2.0, -2.0),
    (-8.0, 2.0, -4.0),
    (3, 0, ZeroDivisionError),
    ("string", 2, TypeError),
    (10, "test", TypeError),
])
def test_divide(x, y, expected):
    if expected == ZeroDivisionError:
        with pytest.raises(ZeroDivisionError):
            divide(x, y)
    elif expected == TypeError:
        with pytest.raises(TypeError):
            divide(x, y)
    else:
        assert divide(x, y) == pytest.approx(expected)
