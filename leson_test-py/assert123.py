def my_num(number):
    return number ** 2


age = 18


def add_num(a, b):
    return a + b


def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == '__main__':
    assert my_num(2) == 4, 'error'
    assert my_num(3) == 9, 'error'
    assert my_num(4) == 16, 'error'
    assert my_num(5) == 25, 'error'
    assert age == 18, 'error'
