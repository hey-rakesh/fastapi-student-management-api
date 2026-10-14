
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

students = {
    1: {"student_id": 1, "name": "Rakesh", "age": 18, "course": "Btech"},
    2: {"student_id": 2, "name": "Vishal", "age": 19, "course": "Mtech"}
}
def get_student(student_id:int):
    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail=f"student with ID {student_id} does not exists"
        )

    return students[student_id]

def get_all_students():
    return list(students.values())


def create_student(Student):
    student_id=Student.student_id

    if student_id in students:
        raise HTTPException(
            status_code=409,
            detail=f"Student with {student_id} already exists"
        )

    students[student_id] = Student.model_dump()

    return students[student_id]
    