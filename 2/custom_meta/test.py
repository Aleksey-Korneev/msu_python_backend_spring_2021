import unittest

from custom_meta import CustomMeta


class TestClass(metaclass=CustomMeta):
    field = 'value'

    def __init__(self):
        pass

    def method(self):
        return self.field


class FieldsNameTest(unittest.TestCase):
    def test_correct(self):
        self.assertTrue(
            hasattr(TestClass, 'custom_field')
        )

    def test_incorrect(self):
        self.assertFalse(
            hasattr(TestClass, 'field')
        )


class MethodsNameTest(unittest.TestCase):
    def setUp(self):
        self.instance = TestClass()

    def test_correct(self):
        self.assertTrue(
            hasattr(TestClass, 'custom_method')
        )

    def test_incorrect(self):
        self.assertFalse(
            hasattr(TestClass, 'method')
        )


class ClassNameTest(unittest.TestCase):
    def test_correct(self):
        self.assertEqual(
            TestClass.__name__,
            'CustomTestClass'
        )

    def test_incorrect(self):
        self.assertNotEqual(
            TestClass.__name__,
            'TestClass'
        )


class MagicMethodsNameTest(unittest.TestCase):
    def setUp(self):
        self.instance = TestClass()

    def test_correct(self):
        self.assertTrue(
            hasattr(TestClass, '__init__')
        )

    def test_incorrect(self):
        self.assertFalse(
            hasattr(TestClass, 'custom__init__')
        )


if __name__ == '__main__':
    unittest.main()
