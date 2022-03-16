import unittest
from datetime import date
from Subject import Subject
from Specialization import Specialization
from Exam import Exam


class TestClassExam (unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        subject = Subject("1", "2", 3, 4, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович")
        self.assertEqual(subject, exam.subject)
        self.assertEqual(examDate, exam.examDate)
        self.assertEqual(2022, exam.year)
        self.assertEqual("Иванов Иван Иванович", exam.lecturerFio)


if __name__ == '__main__':
    unittest.main()
