from dataclasses import dataclass


@dataclass
class Specialization:
    name: str

    def __init__(self, value_name: str):
        self.name = value_name