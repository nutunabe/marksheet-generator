from student import Student
from group import Group
from subject import Subject
from specialization import Specialization
from exam import Exam
from exam_points import ExamPoints


def add(arg, institute):
    if arg == 'student':
        fio = input("ФИО: ")
        code = int(input("Номер студенческого билета: "))
        student = Student(fio, code)
        institute.add_student(student)
        print(institute.get_student(code))
    elif arg == 'group':
        name = input("Название группы: ")
        year = int(input("Год: "))
        specialization_name = input("Специализация: ")
        specialization = institute.get_specialization(specialization_name)
        if specialization == None:
            specialization = Specialization(specialization_name)
            institute.add_specialization(specialization)
        group = Group(name, year, specialization)
        institute.add_group(group)
        print(institute.get_group(name))
