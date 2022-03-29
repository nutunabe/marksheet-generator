from dataclasses import dataclass


@dataclass
class Student:
    code: int
    fio: str

    def __init__(self, fio: str, code: int):
        self.code = code
        self.fio = fio
