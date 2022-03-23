from dataclasses import dataclass
from Specialization import Specialization


@dataclass
class Subject:
    code: str
    name: str
    semester: int
    hours: int
    specialization: Specialization

    def __init__(self, value_code: str, value_name: str, value_semester: int, value_hours: int, value_specialization: Specialization):
        self.code = value_code
        self.name = value_name
        self.semester = value_semester
        self.hours = value_hours
        self.specialization = value_specialization
