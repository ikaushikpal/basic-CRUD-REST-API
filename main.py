from typing import List
from fastapi import FastAPI, Depends, status, HTTPException
import schemas, database,student,models
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
import uvicorn


tags_metadata = [
    {
        "name": "BASIC CRUD",
        "description": "Perform CRUD operations on SQLite database using API",
        "externalDocs": {
            "description": "Github Link for code",
            "url": "https://github.com/ikaushikpal/basic-CRUD-REST-API",
        },
    }]

get_db = database.get_db
app = FastAPI(title="CRUD REST API",
    description="This is very basic CRUD REST API based on student database",
    version="1.0.0",
    openapi_tags=tags_metadata
)
models.Base.metadata.create_all(database.engine)


@app.get("/",tags=['Internal'])
@app.get("/home",tags=['Internal'])
def redirect():
    response = RedirectResponse(url='/docs')
    return response


@app.get('/students', status_code=status.HTTP_200_OK, response_model=List[schemas.StudentBase], tags=['BASIC CRUD'])
def getStudents(db: Session = Depends(get_db)):
    '''get all details about all students available in DB'''
    return student.getStudents(db)


@app.post('/student', status_code=status.HTTP_201_CREATED,tags=['BASIC CRUD'])
def addStudent(request: schemas.StudentBase, db: Session = Depends(get_db)):
    '''add a new student in DB'''
    return student.addStudent(request, db)


@app.delete('/student/{uni_roll}', status_code=status.HTTP_204_NO_CONTENT, tags=['BASIC CRUD'])
def deleteStudent(uni_roll: int, db: Session = Depends(get_db)):
    '''delete a student details from DB'''
    return student.deleteStudent(uni_roll, db)


@app.put('/student/{uni_roll}', status_code=status.HTTP_202_ACCEPTED, tags=['BASIC CRUD'])
def updateStudent(uni_roll: int, request: schemas.Student, db: Session = Depends(get_db)):
    '''update specific student details using uni_roll'''
    return student.updateStudent(uni_roll, request, db)


@app.get('/student/{uni_roll}', status_code=status.HTTP_200_OK, response_model=schemas.Student, tags=['BASIC CRUD'])
def showStudent(uni_roll: int, db: Session = Depends(get_db)):
    '''get a single student details'''
    return student.showStudent(uni_roll, db)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=5000)