from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator
import re
from CONST import *


class ValidateData:
    NAME = re.compile(r'^[a-zA-Z]+\s[a-zA-Z]+$')
    UNIROLL = re.compile(r'^[0-9]{1,5}[0-9]{6}$')
    DEPT = re.compile(r'^[a-zA-Z]+$')
    SECTION = re.compile(r'^[0-9]$')


class StudentBase(BaseModel):
    uni_roll:int
    name:str
    dept:str
    section:int

    @validator('name')
    def nameValidator(cls, input_name):
        result = ValidateData.NAME.match(input_name)
        if result is None or len(input_name) > MAX_NAME_LENGTH:
            raise ValueError('Invalid Student Name. Name must contain alteast first name and last name and only characters')
        return input_name.title()

    @validator('uni_roll')
    def uniRollValidator(cls, input_uni_roll):
        string_input_uni_roll = str(input_uni_roll)

        result = ValidateData.UNIROLL.match(string_input_uni_roll)
        if result is None:
            raise ValueError('Invalid University Roll')
        return input_uni_roll

    @validator('dept')
    def deptValidator(cls, input_dept):
        result = ValidateData.DEPT.match(input_dept)
        if result is None or len(input_dept) > MAX_DEPT_LENGTH:
            raise ValueError('Invalid Dept. Use dept names as CSE/IT/ECE etc')
        return input_dept
    
    @validator('section')
    def sectionValidator(cls, input_section):
        string_input_section = str(input_section)

        result = ValidateData.SECTION.match(string_input_section)
        if result is None:
            raise ValueError('Invalid Section. Section only take 1 to 9')
        return input_section
    class Config():
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Kaushik Pal",
                "uni_roll": 12000119098,
                "dept":'CSE',
                "section" : 2
            }
        }


class Student(BaseModel):
    name:str
    dept:str
    section:int

    @validator('name')
    def nameValidator(cls, input_name):
        result = ValidateData.NAME.match(input_name)
        if result is None:
            raise ValueError('Invalid Student Name. Name must contain alteast first name and last name and only characters')
        return input_name.title()

    @validator('dept')
    def deptValidator(cls, input_dept):
        result = ValidateData.DEPT.match(input_dept)
        if result is None:
            raise ValueError('Invalid Dept. Use dept names as CSE/IT/ECE etc')
        return input_dept
    
    @validator('section')
    def sectionValidator(cls, input_section):
        string_input_section = str(input_section)

        result = ValidateData.SECTION.match(string_input_section)
        if result is None:
            raise ValueError('Invalid Section. Section only take 1 to 9')
        return input_section
    class Config():
        orm_mode = True
        schema_extra = {
            "example": {
                "name": "Kaushik Pal",
                "dept":'CSE',
                "section" : 2
            }
        }
