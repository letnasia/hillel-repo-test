from peewee import fn
from random import randint, choice

from db import Student, Teacher, Mark

students = Student.select()
teachers = Teacher.select()

for _ in range(100):
    # Get random student and teacher
    student = choice(students)
    teacher = choice(teachers)

    # Generate mark
    Mark.create(student=student, teacher=teacher, value=randint(60, 100))
