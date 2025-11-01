import pytest

def square(x):
    return x * x

def cube(x):
    return x * x * x

def fifth_power(x):
    return x ** 5   

def test_square():
    assert square(2) == 4
    assert square(-3) == 9
    assert square(0) == 0

def test_cube():
    assert cube(2) == 8
    assert cube(-3) == -27
    assert cube(0) == 0

def test_fifth_power():
    assert fifth_power(2) == 32
    assert fifth_power(-3) == -243
    assert fifth_power(0) == 0

def test_invalid_input():
    with pytest.raises(TypeError):
        square("string")