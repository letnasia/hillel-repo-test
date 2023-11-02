from flask import request


def deserialize_student_data():
    data = request.get_json()

    name = data.get("name")
    age = data.get("age")

    return {
        "name": name,
        "age": age
    }


def deserialize_teacher_data():
    data = request.get_json()

    name = data.get("name")
    subject = data.get("subject")
    degree = data.get("degree")

    return {
        "name": name,
        "subject": subject,
        "degree": degree,
    }


def deserialize_teacher_update_data():
    data = request.get_json()
    fields = ["name", "subject", "degree"]
    return {
        k: v
        for k, v in data.items()
        if k in fields
    }


def deserialize_mark_data():
    data = request.get_json()

    student_id = data.get("student_id")
    value = data.get("value")
    teacher_id = data.get("teacher_id")

    return {
        "student_id": student_id,
        "value": value,
        "teacher_id": teacher_id,
   }