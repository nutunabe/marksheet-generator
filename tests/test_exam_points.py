import unittest
from exam_points import ExamPoints
from student import Student
from institute import Institute


class TestClassExamPoints(unittest.TestCase):
    def test_1(self):
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65.4, 12.3)
        self.assertEqual(student, examPoints.student)
        self.assertEqual(65.4, examPoints.inPoints)
        self.assertEqual(12.3, examPoints.examPoints)


class TestAddExamResult(unittest.TestCase):
    def test_1(self):  # CORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65.4, 12.3)
        institute = Institute()
        institute.add_exam_result(examPoints)
        self.assertEqual(len(institute.exam_results), 1)

    def test_2(self):  # INCORRECT
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(None)  # exam points is null
        self.assertTrue(
            'Exam points must not be null' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_3(self):  # CORRECT
        student1 = Student("Федоров Байытаан Павлович", 123456)
        student2 = Student("Иванов Иван Иванович", 456789)
        examPoints1 = ExamPoints(student1, 65.4, 12.3)
        examPoints2 = ExamPoints(student2, 45.6, 23.1)
        institute = Institute()
        institute.add_exam_result(examPoints1)
        institute.add_exam_result(examPoints2)
        self.assertEqual(len(institute.exam_results), 2)

    def test_4(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65.4, 12.3)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
            institute.add_exam_result(examPoints)  # re-entry
        self.assertTrue(
            'This element already exists' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 1)

    def test_5(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(1, 65.4, 12.3)  # student type error
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue(
            'Wrong type: must be Student' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_6(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65, 12.3)  # inpoints is not float
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue('Wrong type: must be float' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_7(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65.4, 12)  # exampoints is not float
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue('Wrong type: must be float' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_8(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)  # inpoints > 70
        examPoints = ExamPoints(student, 85.4, 12.3)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue(
            'In points must be lower than 70' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)

    def test_9(self):  # INCORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        examPoints = ExamPoints(student, 65.4, 42.3)  # exampoints > 30
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_exam_result(examPoints)
        self.assertTrue(
            'Exam points must be lower than 30' in str(context.exception))
        self.assertEqual(len(institute.exam_results), 0)


class TestGetExamResults(unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        subject = Subject("Б1.Б.22", "Основы программирования",
                          1, 144, specialization)
        examDate = date(2022, 5, 5)
        exam = Exam(subject, examDate, 2022, "Иванов Иван Иванович")
        institute = Institute()
        examResults = institute.get_exam_results(exam)
        self.assertIn(type(examResults), [list, type(None)])

    def test_2(self):
        exam = "abcd"
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.get_exam_results(exam)

    def test_3(self):
        exam = None
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.get_exam_results(exam)


if __name__ == '__main__':
    unittest.main()
