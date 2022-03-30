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

    def add_student(self, student: Student):
        if student == None:
            raise Exception("Student must not be null")
        if student.fio == "":
            raise Exception("Empty name")
        if " " in student.fio:
            name = student.fio.split(' ')
            for x in name:
                if not x.istitle():
                    raise Exception("Incorrect name")
        else:
            raise Exception("Incorrect name")
        for x in self.students:
            if x == student:
                raise Exception("This element already exists")
        if type(student.code) != int:
            raise Exception("Wrong type: must be integer")
        if student.code / 100000 < 1:
            raise Exception("Student code is not 6-digit")
        self.students.append(student)

    def add_group(self, group: Group):
        if group == None:
            raise Exception("Group must not be null")
        if group.name == "":
            raise Exception("Empty name")
        for x in self.groups:
            if x == group:
                raise Exception("This element already exists")
        self.groups.append(group)

    def add_subject(self, subject: Subject):
        if subject == None:
            raise Exception("Subject must not be null")
        if subject.code == "":
            raise Exception("Empty subject code")
        if subject.name == "":
            raise Exception("Empty subject name")
        if type(subject.semester) != int or type(subject.hours) != int:
            raise Exception("Wrong type: must be integer")
        for x in self.subjects:
            if x == subject:
                raise Exception("This element already exists")
        self.subjects.append(subject)

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

    def add_exam(self, exam: Exam):
        if exam == None:
            raise Exception("Exam must not be null")
        for x in self.exams:
            if x == exam:
                raise Exception("This element already exists")
        self.exams.append(exam)

    def add_exam_result(self, exam_result: ExamPoints):
        if exam_result == None:
            raise Exception("Exam points must not be null")
        if type(exam_result.student) != Student:
            raise Exception("Wrong type: must be Student")
        if type(exam_result.inPoints) != float or type(exam_result.examPoints) != float:
            raise Exception("Wrong type: must be float")
        if exam_result.inPoints > 70.0:
            raise Exception("In points must be lower than 70")
        if exam_result.examPoints > 30.0:
            raise Exception("Exam points must be lower than 30")
        for x in self.exam_results:
            if x == exam_result:
                raise Exception("This element already exists")
        self.exam_results.append(exam_result)

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
