from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    major: str

@app.get("/")
async def read_root():
    return{"message": "Welcome to the Umass Web App API"}

@app.get("/courses")
async def get_courses():
    return {"courses": ["Math 101", "Biology 201", "History 301"]}

@app.get("/students/{student_id}")
async def get_student(student_id: int):
    return {"student_id": student_id, "name": "John Doe", "major": "Computer Science"}


@app.post("/students/")
async def create_student(student: Student):
    return {"message": "Student created", "student": student}