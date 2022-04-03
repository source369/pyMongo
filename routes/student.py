
from fastapi import APIRouter
from models.student import Student
from config.database import con
from schemas.student import student_entity,student_list

student_router= APIRouter()

# hello app
@student_router.get('/hello')
async def hello():
    return "Welcome to App"

# Get all student
@student_router.get('/students')
async def find_all_student():
    return student_list(con.local.student.find())


# Create Student
@student_router.post('/students')
async def save_student(student:Student):
    con.local.student.insert_one(dict(student))
    return student_list(con.local.student.find())
