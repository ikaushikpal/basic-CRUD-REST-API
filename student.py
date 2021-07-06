from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status


def getStudents(db: Session):
    students = db.query(models.StudentDB).all()
    return students


def addStudent(request: schemas.StudentBase, db: Session):
    newStudent = models.StudentDB(name=request.name, uni_roll=request.uni_roll, dept=request.dept, section=request.section)

    db.add(newStudent)
    db.commit()
    db.refresh(newStudent)

    return newStudent


def deleteStudent(uni_roll: int, db: Session):
    student = db.query(models.StudentDB).filter(models.StudentDB.uni_roll == uni_roll)

    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Student with uni roll no {uni_roll} not found")

    student.delete(synchronize_session=False)
    db.commit()



def updateStudent(uni_roll: int, request: schemas.Student, db: Session):
    student = db.query(models.StudentDB).filter(models.StudentDB.uni_roll == uni_roll)

    if not student.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Blog with id {uni_roll} not found")

    tempStudent = schemas.StudentBase(uni_roll=uni_roll, name=request.name, dept=request.dept, section=request.section)

    student.update({'name':request.name, 'dept':request.dept,'section':request.section})
    db.commit()
    return tempStudent


def showStudent(uni_roll: int, db: Session):
    student = db.query(models.StudentDB).filter(models.StudentDB.uni_roll == uni_roll).first()

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"student with the uni roll no {uni_roll} is not available")


    return student
