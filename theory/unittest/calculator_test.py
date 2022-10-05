from unittest import TestCase, main
from calculator import calculator


class CalculatorTest(TestCase):
    def test_plus(self):
        self.assertEqual(calculator('2+2'), 4)

    # def test_plus1(self):
    #     self.assertEqual(calculator('2+2'), 100)

    def test_minus(self):
        self.assertEqual(calculator('2-2'), 0)

    def test_multi(self):
        self.assertEqual(calculator('2*2'), 4)

    def test_divide(self):
        self.assertEqual(calculator('2/2'), 1.0)

    def test_many_signs(self):
        with self.assertRaises(ValueError) as e:
            calculator('2+3*10')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_no_ints(self):
        with self.assertRaises(ValueError) as e:
            calculator('2.3*3.4')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])

    def test_strings(self):
        with self.assertRaises(ValueError) as e:
            calculator('a+b')
        self.assertEqual('Выражение должно содержать 2 целых числа и 1 знак', e.exception.args[0])


if __name__ == '__main__':
    main()
