from student import Student
from group import Group
from subject import Subject
from specialization import Specialization
from exam import Exam
from exam_points import ExamPoints

def get(arg, institute):
    if arg == 'student':
        code = int(input("Номер студенческого билета: "))
        print(institute.get_student(code))