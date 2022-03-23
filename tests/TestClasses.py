import unittest
from Classes import *
from Student import Student
from Subject import Subject
from Specialization import Specialization


class TestClassClasses (unittest.TestCase):
    def test_getSpecialization(self):
        spec_list = []
        spec_list.append(Specialization("ФИИТ"))
        spec_list.append(Specialization("ИВТ"))
        spec_list.append(Specialization("НОД"))

        specs = Specializations(spec_list)
        self.assertEqual("ФИИТ", specs.GetSpecialization("ФИИТ").name)
        self.assertEqual("ИВТ", specs.GetSpecialization("ИВТ").name)
        self.assertEqual("НОД", specs.GetSpecialization("НОД").name)

    def test_getStudent(self):
        students_list = []
        students_list.append(Student("Федоров Байытаан", 123456))
        students_list.append(Student("Иванов Иван", 234567))
        students_list.append(Student("Петров Петр", 345678))
        students_list.append(Student("Алексеев Алексей", 456789))

        students = Students(students_list)
        self.assertEqual(345678, students.GetStudent("Петров Петр").code)
        self.assertEqual("Петров Петр", students.GetStudent("Петров Петр").fio)
        self.assertEqual(123456, students.GetStudent("Федоров Байытаан").code)
        self.assertEqual("Федоров Байытаан",
                         students.GetStudent("Федоров Байытаан").fio)
        self.assertEqual(456789, students.GetStudent("Алексеев Алексей").code)
        self.assertEqual("Алексеев Алексей",
                         students.GetStudent("Алексеев Алексей").fio)
        self.assertEqual(234567, students.GetStudent("Иванов Иван").code)
        self.assertEqual("Иванов Иван", students.GetStudent("Иванов Иван").fio)

    def test_getSubject(self):
        spec_fiit = Specialization("ФИИТ")
        spec_ivt = Specialization("ИВТ")
        subjects_list = []
        subjects_list.append(Subject("11", "1", 2, 3, spec_fiit))
        subjects_list.append(Subject("22", "2", 3, 4, spec_fiit))
        subjects_list.append(Subject("33", "3", 4, 5, spec_ivt))
        subjects_list.append(Subject("44", "4", 5, 6, spec_fiit))
        subjects_list.append(Subject("55", "5", 6, 7, spec_ivt))
        subjects_list.append(Subject("66", "6", 7, 8, spec_fiit))

        subjects = Subjects(subjects_list)
        # 1
        self.assertEqual("11", subjects.GetSubject("1").code)
        self.assertEqual("1", subjects.GetSubject("1").name)
        self.assertEqual(2, subjects.GetSubject("1").semester)
        self.assertEqual(3, subjects.GetSubject("1").hours)
        self.assertEqual(spec_fiit, subjects.GetSubject("1").specialization)
        # 2
        self.assertEqual("22", subjects.GetSubject("2").code)
        self.assertEqual("2", subjects.GetSubject("2").name)
        self.assertEqual(3, subjects.GetSubject("2").semester)
        self.assertEqual(4, subjects.GetSubject("2").hours)
        self.assertEqual(spec_fiit, subjects.GetSubject("2").specialization)
        # 3
        self.assertEqual("33", subjects.GetSubject("3").code)
        self.assertEqual("3", subjects.GetSubject("3").name)
        self.assertEqual(4, subjects.GetSubject("3").semester)
        self.assertEqual(5, subjects.GetSubject("3").hours)
        self.assertEqual(spec_ivt, subjects.GetSubject("3").specialization)
        # 4
        self.assertEqual("44", subjects.GetSubject("4").code)
        self.assertEqual("4", subjects.GetSubject("4").name)
        self.assertEqual(5, subjects.GetSubject("4").semester)
        self.assertEqual(6, subjects.GetSubject("4").hours)
        self.assertEqual(spec_fiit, subjects.GetSubject("4").specialization)
        # 5
        self.assertEqual("55", subjects.GetSubject("5").code)
        self.assertEqual("5", subjects.GetSubject("5").name)
        self.assertEqual(6, subjects.GetSubject("5").semester)
        self.assertEqual(7, subjects.GetSubject("5").hours)
        self.assertEqual(spec_ivt, subjects.GetSubject("5").specialization)
        # 6
        self.assertEqual("66", subjects.GetSubject("6").code)
        self.assertEqual("6", subjects.GetSubject("6").name)
        self.assertEqual(7, subjects.GetSubject("6").semester)
        self.assertEqual(8, subjects.GetSubject("6").hours)
        self.assertEqual(spec_fiit, subjects.GetSubject("6").specialization)
