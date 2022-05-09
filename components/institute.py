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
        if student.code == None:
            raise Exception("Student code must not be null")
        if type(student.code) != int:
            raise Exception("Wrong type: must be integer")
        if student.code < 0:
            raise Exception("Student code must not be < 0")
        if len(str(student.code)) != 6:
            raise Exception("Student code is not 6-digit")
        if student.fio == None:
            raise Exception("Student name must not be null")
        if type(student.fio) != str:
            raise Exception("Wrong type: must be str")
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
        self.students.append(student)

    def add_group(self, group: Group):
        if group == None:
            raise Exception("Group must not be null")
        if group.name == "":
            raise Exception("Empty name")
        for x in self.groups:
            if x == group:
                raise Exception("This element already exists")
        exception = ""
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

    def get_student(self, code: int) -> Student:
        student = None
        if code == None:
            raise Exception()
        if type(code) != int:
            raise Exception()
        if code < 0:
            raise Exception()
        if len(str(code)) != 6:
            raise Exception()
        for x in self.students:
            if x.code == code:
                student = x
        return student

    def get_group(self, name: str) -> Group:
        group = None
        if name == None:
            raise Exception()
        if type(name) != str:
            raise Exception()
        if name == "":
            raise Exception()
        for x in self.groups:
            if x.name == name:
                group = x
        return group

    def get_subject(self, name: str):
        subject = None
        if name == None:
            raise Exception()
        if type(name) != str:
            raise Exception()
        if name == "":
            raise Exception()
        for x in self.subjects:
            if x.name == name:
                subject = x
        return subject

    def get_specialization(self, name: str):
        specialization = None
        if name == None:
            raise Exception()
        if type(name) != str:
            raise Exception()
        if name == "":
            raise Exception()
        for x in self.specializations:
            if x.name == name:
                specialization = x
        return specialization

    def get_exam(self, group: str, subject: str, date: Date):
        exam = None
        if group == "" or subject == "" or date == "":
            raise Exception()
        if type(group) != str or type(subject) != str or type(date) != Date:
            raise Exception()
        if date > Date(2022, 5, 31) or date < Date(1934, 1, 1):
            raise Exception()
        for x in self.exams:
            if x.examDate == date and x.subject.name == subject:
                exam = x
        return exam

    def get_exam_results(self, exam: Exam):
        exam_results = None
        if type(exam) != Exam:
            raise Exception()
        for x in self.exam_results:
            if x.exam.group.name == exam.group.name:
                exam_results = x
        return exam_results
