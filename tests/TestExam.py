import unittest
import os
import sys
PROJECT_PATH = os.getcwd()
print(PROJECT_PATH)
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "classes"
)
sys.path.append(SOURCE_PATH)
from datetime import date
from Subject import Subject
from Specialization import Specialization
from Exam import Exam


class TestClassExam (unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        subject = Subject("1", "2", 3, 4, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(Subject, examDate, 2022, "Иванов Иван Иванович")
        self.assertEqual(Subject, exam.subject)
        self.assertEqual(examDate, exam.examDate)
        self.assertEqual(2022, exam.year)
        self.assertEqual("Иванов Иван Иванович", exam.lecturerFio)


if __name__ == '__main__':
    unittest.main()
