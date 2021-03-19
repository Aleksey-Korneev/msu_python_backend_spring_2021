import unittest

from my_list import MyList


class AddTest(unittest.TestCase):
    def setUp(self):
        self.x = MyList([1, 2, 3])
        self.y = MyList([5, 6])

    def test_basic(self):
        self.assertEqual(
            self.x + self.y,
            MyList([6, 8, 3])
        )

    def test_type(self):
        self.assertTrue(
            isinstance(self.x + self.y, MyList)
        )

    def test_add_list(self):
        self.assertEqual(
            self.x + [5, 6],
            MyList([6, 8, 3])
        )

    def test_radd_list(self):
        self.assertEqual(
            [1, 2, 3] + self.y,
            MyList([6, 8, 3])
        )

    def test_type_add_list(self):
        self.assertTrue(
            isinstance(self.x + [5, 6], MyList)
        )

    def test_type_radd_list(self):
        self.assertTrue(
            isinstance([1, 2, 3] + self.y, MyList)
        )

    def test_immutability(self):
        before = len(self.y)
        self.x + self.y
        after = len(self.y)

        self.assertEqual(before, after)


class SubTest(unittest.TestCase):
    def setUp(self):
        self.x = MyList([1, 2, 3])
        self.y = MyList([5, 6])

    def test_basic(self):
        self.assertEqual(
            self.x - self.y,
            MyList([-4, -4, 3])
        )

    def test_type(self):
        self.assertIs(
            type(self.x - self.y),
            MyList
        )

    def test_sub_list(self):
        self.assertEqual(
            self.x - [5, 6],
            MyList([-4, -4, 3])
        )

    def test_rsub_list(self):
        self.assertEqual(
            [1, 2, 3] - self.y,
            MyList([-4, -4, 3])
        )

    def test_type_sub_list(self):
        self.assertTrue(
            isinstance(self.x - [5, 6], MyList)
        )

    def test_type_rsub_list(self):
        self.assertTrue(
            isinstance([1, 2, 3] - self.y, MyList)
        )

    def test_immutability(self):
        before = len(self.y)
        self.x - self.y
        after = len(self.y)

        self.assertEqual(before, after)


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
