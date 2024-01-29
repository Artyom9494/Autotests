from unittest import TestCase, main
from assert123 import my_num


class TestFunction(TestCase):
    def test_my_num1(self):
        self.assertEqual(my_num(2), 4)

    def test_my_num2(self):
        self.assertEqual(my_num(3), 9)

    def test_my_num3(self):
        self.assertEqual(my_num(4), 16)


if __name__ == '__main__':
    main()
