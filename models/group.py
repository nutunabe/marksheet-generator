from dataclasses import dataclass
from specialization import Specialization


@dataclass
class Group:
    name: str
    year: int
    specialization: Specialization

    def __init__(self, name: str, year: int, specialization: Specialization):
        self.name = name
        self.year = year
        self.specialization = specialization
