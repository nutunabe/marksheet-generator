from dataclasses import dataclass
from student import Student

@dataclass
class ExamPoints:
    student: Student
    inPoints: float
    examPoints: float

    def __init__(self, student: Student, inPoints: float, examPoints: float):
        self.student = student
        self.inPoints = inPoints
        self.examPoints = examPoints
