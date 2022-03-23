from dataclasses import dataclass
from Student import Student

@dataclass
class ExamPoints:
    student: Student
    inPoints: float
    examPoints: float

    def __init__(self, value_student: Student, value_inPoints: float, value_examPoints: float):
        self.student = value_student
        self.inPoints = value_inPoints
        self.examPoints = value_examPoints
