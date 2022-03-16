import unittest
from Student import Student


class TestClassStudent (unittest.TestCase):
    def test_1(self):
        student = Student("Федоров Байытаан", 123456)
        self.assertEqual("Федоров Байытаан", student.fio)
        self.assertEqual(123456, student.code)


if __name__ == '__main__':
    unittest.main()
