from dataclasses import dataclass
from Specialization import Specialization


@dataclass
class Group:
    name: str
    year: int
    specialization: Specialization

    def __init__(self, value_name: str, value_year: int, value_specialization: Specialization):
        self.name = value_name
        self.year = value_year
        self.specialization = value_specialization
