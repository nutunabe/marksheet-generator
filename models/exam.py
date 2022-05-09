from dataclasses import dataclass
from subject import Subject
from group import Group
from datetime import date


@dataclass
class Exam:
    subject: Subject
    examDate: date
    year: str
    lecturerFio: str
    group: Group

    def __init__(self, subject: Subject, examDate: date, year: str, lecturerFio: str, group: Group):
        self.subject = subject
        self.examDate = examDate
        self.year = year
        self.lecturerFio = lecturerFio
        self.group = group
