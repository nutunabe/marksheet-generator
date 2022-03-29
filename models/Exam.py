from dataclasses import dataclass
from subject import Subject
from datetime import date


@dataclass
class Exam:
    subject: Subject
    examDate: date
    year: str
    lecturerFio: str

    def __init__(self, subject: Subject, examDate: date, year: str, lecturerFio: str):
        self.subject = subject
        self.examDate = examDate
        self.year = year
        self.lecturerFio = lecturerFio
