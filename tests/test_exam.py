import unittest
from datetime import date
from subject import Subject
from specialization import Specialization
from exam import Exam
from institute import Institute


class TestClassExam(unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        subject = Subject("1", "2", 3, 4, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович")
        self.assertEqual(subject, exam.subject)
        self.assertEqual(examDate, exam.examDate)
        self.assertEqual(2022, exam.year)
        self.assertEqual("Иванов Иван Иванович", exam.lecturerFio)


class TestAddExam(unittest.TestCase):
    def test_1(self):  # CORRECT
        specialization = Specialization("ФИИТ")
        subject = Subject("Б1.Б.22", "Основы программирования",
                          1, 144, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович")
        institute = Institute()
        institute.add_exam(exam)
        self.assertEqual(len(institute.exams), 1)

    def test_2(self):  # INCORRECT
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam(None)  # exam is null
        self.assertTrue('Exam must not be null' in str(context.exception))
        self.assertEqual(len(institute.exams), 0)

    def test_3(self):  # CORRECT
        specialization1 = Specialization("ФИИТ")
        specialization2 = Specialization("ИВТ")
        subject1 = Subject("Б1.Б.22", "Основы программирования",
                           1, 144, specialization1)
        subject2 = Subject("Б1.Б.22", "Основы программирования",
                           1, 144, specialization2)
        examDate = date(2022, 5, 5)
        exam1 = Exam(subject1, examDate, 2022, "Иванов Иван Иванович")
        exam2 = Exam(subject2, examDate, 2022, "Петров Петр Петрович")
        institute = Institute()
        institute.add_exam(exam1)
        institute.add_exam(exam2)
        self.assertEqual(len(institute.exams), 2)

    def test_4(self):  # INCORRECT
        specialization = Specialization("ФИИТ")
        subject = Subject("Б1.Б.22", "Основы программирования",
                          1, 144, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович")
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam(exam)
            institute.add_exam(exam)  # re-entry
        self.assertTrue(
            'This element already exists' in str(context.exception))
        self.assertEqual(len(institute.exams), 1)


if __name__ == '__main__':
    unittest.main()
