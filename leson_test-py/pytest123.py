import pytest
from assert123 import my_num, add_num, divide_numbers


def test_my_num1():
    assert my_num(2) == 4, 'error'


def test_my_num2():
    assert my_num(3) == 9, 'error'


def test_my_num3():
    assert my_num(5) == 25, 'error'


def test_add_numbers():
    assert add_num(2, 3) == 5
    assert add_num(-1, 1) == 0
    assert add_num(0, 0) == 0


def test_divide_numbers():
    assert divide_numbers(6, 2) == 3
    assert divide_numbers(10, 5) == 2
    with pytest.raises(ValueError):
        divide_numbers(10, 0)


if __name__ == '__main__':
    pytest.main()
