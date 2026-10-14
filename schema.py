from pydantic import BaseModel, Field

class Student(BaseModel):
    student_id: int = Field(gt=0)
    name: str = Field(min_length=2)
    age: int = Field(ge=16)
    course: str = Field(...)