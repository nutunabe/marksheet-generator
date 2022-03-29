from dataclasses import dataclass


@dataclass
class Specialization:
    name: str

    def __init__(self, name: str):
        self.name = name
