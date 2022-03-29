from dataclasses import dataclass
from specialization import Specialization


@dataclass
class Subject:
    code: str
    name: str
    semester: int
    hours: int
    specialization: Specialization

    def __init__(self, code: str, name: str, semester: int, hours: int, specialization: Specialization):
        self.code = code
        self.name = name
        self.semester = semester
        self.hours = hours
        self.specialization = specialization
