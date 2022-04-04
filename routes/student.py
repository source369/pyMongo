
from fastapi import APIRouter
from models.student import Student
from config.database import con
from schemas.student import student_entity,student_list
from bson import ObjectId

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


# find Student by ID
@student_router.get("/students/{studentId}")
async def get_student_by_id(studentId):
    return student_entity(con.local.student.find_one({"_id": ObjectId(studentId)}))


# Update Student
@student_router.put("/students/{studentId}")
async def update_student(studentId,stu:Student):
    con.local.student.find_one_and_update(
        {"_id":ObjectId(studentId)},
        {"$set":dict(stu)}
    )
    return student_entity(con.local.student.find_one({"_id":ObjectId(studentId)}))


# Delete Student
@student_router.delete("/students/{studentId}")
async def delete_student(studentId):
    return student_entity(con.local.student.find_one_and_delete({"_id":ObjectId(studentId)}))
