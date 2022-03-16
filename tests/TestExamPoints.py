import unittest
from ExamPoints import ExamPoints
from Student import Student


class TestClassExamPoints (unittest.TestCase):
    def test_1(self):
        student = Student("Федоров Байытаан", 123456)
        examPoints = ExamPoints(student, 12.3, 45.6)
        self.assertEqual(student, examPoints.student)
        self.assertEqual(12.3, examPoints.inPoints)
        self.assertEqual(45.6, examPoints.examPoints)


if __name__ == '__main__':
    unittest.main()
