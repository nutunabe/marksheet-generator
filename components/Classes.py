from collections.abc import Sequence
from student import Student
from subject import Subject
from specialization import Specialization


class Specializations:
    specializations: Sequence[Specialization]

    def __init__(self, value_specializations: Sequence[Specialization]):
        self.specializations = value_specializations

    def GetSpecialization(self, value_name: str) -> Specialization:
        for x in self.specializations:
            if x.name == value_name:
                return x


class Students:
    students: Sequence[Student]

    def __init__(self, value_students: Sequence[Student]):
        self.students = value_students

    def GetStudent(self, value_fio: str) -> Student:
        for x in self.students:
            if x.fio == value_fio:
                return x


class Subjects:
    subjects: Sequence[Subject]

    def __init__(self, value_subjects: Sequence[Subject]):
        self.subjects = value_subjects

    def GetSubject(self, value_name: str) -> Subject:
        for x in self.subjects:
            if x.name == value_name:
                return x
