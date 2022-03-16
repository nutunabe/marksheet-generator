import unittest
from Specialization import Specialization


class TestClassSpecialization (unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        self.assertEqual("ФИИТ", specialization.name)


if __name__ == '__main__':
    unittest.main()
