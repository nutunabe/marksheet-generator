import unittest
import os
import sys
PROJECT_PATH = os.getcwd()
print(PROJECT_PATH)
SOURCE_PATH = os.path.join(
    PROJECT_PATH, "classes"
)
sys.path.append(SOURCE_PATH)
from Specialization import Specialization


class TestClassSpecialization (unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        self.assertEqual("ФИИТ", specialization.name)


if __name__ == '__main__':
    unittest.main()
