import unittest
import os
import sys
PROJECT_PATH = os.getcwd()
print(PROJECT_PATH)
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "classes"
)
sys.path.append(SOURCE_PATH)
from Subject import Subject
from Specialization import Specialization


class TestClassSubject (unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        subject = Subject("1", "2", 3, 4, specialization)
        self.assertEqual("1", subject.code)
        self.assertEqual("2", subject.name)
        self.assertEqual(3, subject.semester)
        self.assertEqual(4, subject.hours)
        self.assertEqual(specialization, subject.specialization)


if __name__ == '__main__':
    unittest.main()
