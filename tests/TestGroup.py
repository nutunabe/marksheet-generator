import unittest
from Group import Group
from Specialization import Specialization


class TestClassGroup (unittest.TestCase):
    def test_1(self):
        specialization = Specialization("ФИИТ")
        group = Group("М-ФИИТ-21", 2021, specialization)
        self.assertEqual("М-ФИИТ-21", group.name)
        self.assertEqual(2021, group.year)
        self.assertEqual(specialization, group.specialization)


if __name__ == '__main__':
    unittest.main()
