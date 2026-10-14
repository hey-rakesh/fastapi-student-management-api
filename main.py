
from fastapi import FastAPI
from schema import Student
from model_services import get_student, get_all_students, create_student

app = FastAPI()


@app.get("/")
def greet_api():
    return "good bye"


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.get("/about")
def about():
    return {
        "name": "Student Management System",
        "version": "1.0.0"
    }


@app.get("/students")
def read_students():
    return get_all_students()


@app.get("/students/{student_id}", response_model=Student)
def get_student_id(student_id: int):
    return get_student(student_id)


@app.post("/students", response_model=Student, status_code=201)
def add_student(student_data: Student):
    return create_student(student_data)
