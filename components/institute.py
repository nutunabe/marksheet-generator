from collections.abc import Sequence
from datetime import date as Date
from student import Student
from group import Group
from subject import Subject
from specialization import Specialization
from exam import Exam
from exam_points import ExamPoints


class Institute:
    students: Sequence[Student]
    groups: Sequence[Group]
    subjects: Sequence[Subject]
    specializations: Sequence[Specialization]
    exams: Sequence[Exam]
    exam_results: Sequence[ExamPoints]

    def __init__(self):
        self.students = []
        self.groups = []
        self.subjects = []
        self.specializations = []
        self.exams = []
        self.exam_results = []

    # def add_student(self, student: Student):
    #     # . . .
    #     self.students.append(student)

    # def add_group(self, group: Group):
    #     # . . .
    #     self.groups.append(group)

    # def add_subject(self, subject: Subject):
    #     # . . .
    #     self.subjects.append(subject)

    def add_specialization(self, specialization: Specialization):
        if specialization == None:
            raise Exception("Specialization must not be null")
        if type(specialization) != Specialization:
            raise Exception("Wrong type: must be Specialization")
        if specialization.name == "":
            raise Exception("Empty name")
        for x in self.specializations:
            if x == specialization:
                raise Exception("This element already exists")
        self.specializations.append(specialization)

    # def add_exam(self, exam: Exam):
    #     # . . .
    #     self.exams.append(exam)

    # def add_exam_result(self, exam_result: ExamPoints):
    #     # . . .
    #     self.exam_results.append(exam_result)

    # def get_student(self, code: int):
    #     #  . . .

    # def get_group(self, name: str):
    #     #  . . .

    # def get_subject(self, name: str):
    #     #  . . .

    # def get_specialization(self, name: str):
    #     #  . . .

    # def get_exam(self, group: str, subject: str, date: Date):
    #     #  . . .

    # def get_exam_results(self, exam: Exam):
    #     #  . . .
