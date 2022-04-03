# Schema help to serialisze and also convert mongoDb format into json


def student_entity(db_item)-> dict:
    return {
        "id": str(db_item["_id"]),
        "name": db_item["student_name"],
        "email": db_item["student_email"],
        "phone_no": db_item["student_phone"]
    }

def student_list(db_item_list) -> list:
    stu_list =[]
    for item in db_item_list:
        stu_list.append(student_entity(item))
    return stu_list