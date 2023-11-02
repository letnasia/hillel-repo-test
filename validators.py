from db import Student, Teacher


class ValidationError(Exception):
    pass


def validate_student_data(data):
    name = data.get("name")
    age = data.get("age")

    if not (name and age):
        raise ValidationError("name and age are required")

    if not isinstance(age, int):
        raise ValidationError("age must be integer")
    if not isinstance(name, str):
        raise ValidationError("name must be string")

    if age < 0:
        raise ValidationError("age must be positive")
    if name == "":
        raise ValidationError("name must not be empty")


def validate_teacher_data(data):
    name = data.get("name")
    subject = data.get("subject")
    degree = data.get("degree")

    if not (name and subject and degree):
        raise ValidationError("name, subject and degree are required")

    if not isinstance(name, str):
        raise ValidationError("name must be string")
    if not isinstance(subject, str):
        raise ValidationError("subject must be string")
    if not isinstance(degree, str):
        raise ValidationError("degree must be string")

    if name == "":
        raise ValidationError("name must not be empty")
    if subject == "":
        raise ValidationError("subject must not be empty")
    if degree == "":
        raise ValidationError("degree must not be empty")


def validate_teacher_update_data(data):
    name = data.get("name")
    subject = data.get("subject")
    degree = data.get("degree")

    if not (name or subject or degree):
        raise ValidationError("name, subject and degree are required")

    if name:
        if not isinstance(name, str):
            raise ValidationError("name must be string")
        if name == "":
            raise ValidationError("name must not be empty")

    if subject:
        if not isinstance(subject, str):
            raise ValidationError("subject must be string")
        if subject == "":
            raise ValidationError("subject must not be empty")

    if degree:
        if not isinstance(degree, str):
            raise ValidationError("degree must be string")
        if degree == "":
            raise ValidationError("degree must not be empty")


def validate_mark_data(data):
    student_id = data.get("student_id")
    value = data.get("value")
    teacher_id = data.get("teacher_id")

    if not (student_id and value and teacher_id):
        raise ValidationError("student_id, value and teacher_id are required")

    if not isinstance(student_id, int):
        raise ValidationError("student_id must be integer")
    if not isinstance(value, int):
        raise ValidationError("value must be integer")
    if not isinstance(teacher_id, int):
        raise ValidationError("teacher_id must be integer")

    student = Student.get_or_none(id=student_id)

    if not student:
        raise ValidationError("student with such id does not exist")

    teacher = Teacher.get_or_none(id=teacher_id)

    if not teacher:
        raise ValidationError("teacher with such id does not exist")

    if value < 0:
        raise ValidationError("value must be positive")

    return data
