import unittest
from student import Student
from institute import Institute


class TestClassStudent(unittest.TestCase):
    def test_1(self):
        student = Student("Федоров Байытаан", 123456)
        self.assertEqual("Федоров Байытаан", student.fio)
        self.assertEqual(123456, student.code)


class TestAddStudent(unittest.TestCase):
    def test_1(self):  # CORRECT
        student = Student("Федоров Байытаан Павлович", 123456)
        institute = Institute()
        institute.add_student(student)
        self.assertEqual(len(institute.students), 1)

    def test_2(self):  # INCORRECT
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(None)  # student is null
        self.assertTrue('Student must not be null' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_3(self):  # INCORRECT
        student = Student("", 123456)  # empty student name
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue('Empty name' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_4(self):  # INCORRECT
        student = Student("ФедоровБайытаанПавлович",
                          123456)  # incorrect student name
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue('Incorrect name' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_5(self):  # CORRECT
        student1 = Student("Федоров Байытаан Павлович", 123456)
        student2 = Student("Иванов Иван Иванович", 456789)
        institute = Institute()
        institute.add_student(student1)
        institute.add_student(student2)
        self.assertEqual(len(institute.students), 2)

    def test_6(self):  # INCORRECT
        student1 = Student("Федоров Байытаан Павлович", 123456)
        student2 = Student("Федоров Байытаан Павлович", 123456)  # re-entry
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student1)
            institute.add_student(student2)
        self.assertTrue(
            'This element already exists' in str(context.exception))
        self.assertEqual(len(institute.students), 1)

    def test_7(self):  # INCORRECT
        # wrong student code type
        student = Student("Федоров Байытаан Павлович", "123456")
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue(
            'Wrong type: must be integer' in str(context.exception))
        self.assertEqual(len(institute.students), 0)

    def test_8(self):  # INCORRECT
        # student code is not 6-digit
        student = Student("Федоров Байытаан Павлович", 1)
        institute = Institute()
        with self.assertRaises(Exception) as context:
            institute.add_student(student)
        self.assertTrue(
            'Student code is not 6-digit' in str(context.exception))
        self.assertEqual(len(institute.students), 0)


if __name__ == '__main__':
    unittest.main()
