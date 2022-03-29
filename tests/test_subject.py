import unittest
from subject import Subject
from specialization import Specialization
from institute import Institute


class TestClassSubject(unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        subject = Subject("1", "2", 3, 4, specialization)
        self.assertEqual("1", subject.code)
        self.assertEqual("2", subject.name)
        self.assertEqual(3, subject.semester)
        self.assertEqual(4, subject.hours)
        self.assertEqual(specialization, subject.specialization)


# class TestAddSubject(unittest.TestCase):
#     def test_1(self):  # CORRECT
#         specialization = Specialization("ФИИТ")
#         subject = Subject("Б1.Б.22", "Основы программирования",
#                           1, 144, specialization)
#         institute = Institute()
#         institute.add_subject(subject)
#         self.assertEqual(len(institute.subjects), 1)

#     def test_2(self):  # INCORRECT
#         institute = Institute()
#         institute.add_subject(None)  # subject is null
#         self.assertEqual(len(institute.subjects), 1)

#     def test_3(self):  # INCORRECT
#         specialization = Specialization("ФИИТ")
#         subject = Subject("", "Основы программирования", 1,
#                           144, specialization)  # empty subject code
#         institute = Institute()
#         institute.add_subject(subject)
#         self.assertEqual(len(institute.subjects), 1)

#     def test_4(self):  # INCORRECT
#         specialization = Specialization("ФИИТ")
#         subject = Subject("Б1.Б.22", "", 1, 144,
#                           specialization)  # empty subject name
#         institute = Institute()
#         institute.add_subject(subject)
#         self.assertEqual(len(institute.subjects), 1)

#     def test_5(self):  # INCORRECT
#         specialization = Specialization("ФИИТ")
#         subject = Subject("Б1.Б.22", "Основы программирования",
#                           "1", 144, specialization)  # wrong semester type
#         institute = Institute()
#         institute.add_subject(subject)
#         self.assertEqual(len(institute.subjects), 1)

#     def test_6(self):  # INCORRECT
#         specialization = Specialization("ФИИТ")
#         subject = Subject("Б1.Б.22", "Основы программирования",
#                           1, "144", specialization)  # wrong hours type
#         institute = Institute()
#         institute.add_subject(subject)
#         self.assertEqual(len(institute.subjects), 1)

#     def test_7(self):  # CORRECT
#         specialization1 = Specialization("ФИИТ")
#         specialization2 = Specialization("ИВТ")
#         subject1 = Subject(
#             "Б1.Б.22", "Основы программирования", 1, 144, specialization1)
#         subject2 = Subject(
#             "Б1.Б.22", "Основы программирования", 1, 144, specialization2)
#         institute = Institute()
#         institute.add_subject(subject1)
#         institute.add_subject(subject2)
#         self.assertEqual(len(institute.subjects), 2)

#     def test_8(self):  # INCORRECT
#         specialization = Specialization("ФИИТ")
#         subject = Subject("Б1.Б.22", "Основы программирования",
#                           1, 144, specialization)
#         institute = Institute()
#         institute.add_subject(subject)
#         institute.add_subject(subject)  # re-entry
#         self.assertEqual(len(institute.subjects), 2)


if __name__ == '__main__':
    unittest.main()
