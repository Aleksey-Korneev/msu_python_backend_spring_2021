import unittest

from my_list import MyList


class ArithmeticTest(unittest.TestCase):
    def setUp(self):
        self.x = MyList([1, 2, 3])
        self.y = MyList([5, 6])

    def test_add(self):
        self.assertEqual(
            self.x + self.y,
            MyList([6, 8, 3])
        )

    def test_sub(self):
        self.assertEqual(
            self.x - self.y,
            MyList([-4, -4, 3])
        )

    def test_add_type(self):
        self.assertIs(
            type(self.x + self.y),
            MyList
        )

    def test_sub_type(self):
        self.assertIs(
            type(self.x - self.y),
            MyList
        )

    def test_immutability(self):
        z = self.x + self.y

        self.assertEqual(self.y, MyList([5, 6]))


class ComparisonTest(unittest.TestCase):
    def test_equal(self):
        x = MyList([1, 2, 3])
        y = MyList([3, 2, 1])

        self.assertTrue(x == y)

    def test_less(self):
        x = MyList([1, 2])
        y = MyList([3, 2, 1])

        self.assertTrue(x < y)

    def test_not_equal(self):
        x = MyList([1, 2])
        y = MyList([3, 2, 1])

        self.assertTrue(x != y)

    def test_less_or_equal(self):
        x = MyList([1, 2])
        y = MyList([3, 2, 1])

        self.assertTrue(x <= y)


if __name__ == '__main__':
    unittest.main()
