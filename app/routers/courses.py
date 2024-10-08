from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.course import CourseCreate, CourseUpdate
from app.schemas.user import CourseResponse
from app.crud.course import create_course, get_course, get_courses, update_course, delete_course
from app.utils import oauth2
from app.utils.dependency import get_db

router = APIRouter()

# Create Course
@router.post("/course/", response_model=CourseResponse)
def create_course_route(course: CourseCreate, db: Session = Depends(get_db), get_current_user: CourseResponse = Depends(oauth2.get_current_user)):
    return create_course(db, course)

# Read Course by ID
@router.get("/course/{course_code}", response_model=CourseResponse)
def read_course(course_code: str, db: Session = Depends(get_db), get_current_user: CourseResponse = Depends(oauth2.get_current_user)):
    return get_course(db, course_code)

# Read All Courses
@router.get("/courses/", response_model=list[CourseResponse])
def read_courses(db: Session = Depends(get_db), get_current_user: CourseResponse = Depends(oauth2.get_current_user)):
    return get_courses(db)

# Update Course
@router.put("/course/{course_code}", response_model=CourseResponse)
def update_course_route(course_code: str, course: CourseUpdate, db: Session = Depends(get_db), get_current_user: CourseResponse = Depends(oauth2.get_current_user)):
    return update_course(db, course_code, course)

# Delete Course (Soft Delete)
@router.delete("/course/{course_code}")
def delete_course_route(course_code: str, db: Session = Depends(get_db), get_current_user: CourseResponse = Depends(oauth2.get_current_user)):
    return delete_course(db, course_code)
