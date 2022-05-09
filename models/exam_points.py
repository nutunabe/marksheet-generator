from dataclasses import dataclass
from student import Student
from exam import Exam


@dataclass
class ExamPoints:
    student: Student
    inPoints: float
    examPoints: float
    exam: Exam

    def __init__(self, student: Student, inPoints: float, examPoints: float, exam: Exam):
        self.student = student
        self.inPoints = inPoints
        self.examPoints = examPoints
        self.exam = exam
