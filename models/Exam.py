from dataclasses import dataclass
from Subject import Subject
from datetime import date


@dataclass
class Exam:
    subject: Subject
    examDate: date
    year: str
    lecturerFio: str

    def __init__(self, value_subject: Subject, value_examDate: date, value_year: str, value_lecturerFio: str):
        self.subject = value_subject
        self.examDate = value_examDate
        self.year = value_year
        self.lecturerFio = value_lecturerFio
