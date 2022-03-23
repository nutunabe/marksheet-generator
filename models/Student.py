from dataclasses import dataclass


@dataclass
class Student:
    code: int
    fio: str

    def __init__(self, value_fio: str, value_code: int):
        self.code = value_code
        self.fio = value_fio
