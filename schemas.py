from typing import List, Optional
from pydantic import BaseModel, ValidationError, validator
import re


NAME = re.compile(r'^[a-zA-Z]+\s[a-zA-Z]+$')
UNIROLL = re.compile(r'^[0-9]{1,5}[0-9]{6}$')
DEPT = re.compile(r'^[a-zA-Z]+$')
SECTION = re.compile(r'^[0-9]$')


class StudentBase(BaseModel):
    name:str
    uni_roll:int
    dept:str
    section:int

    @validator('name')
    def nameValidator(cls, input_name):
        result = NAME.match(input_name)
        if result is None:
            raise ValueError('Invalid Student Name. Name must contain alteast first name and last name')
        return input_name.title()

    @validator('uni_roll')
    def uniRollValidator(cls, input_uni_roll):
        string_input_uni_roll = str(input_uni_roll)

        result = UNIROLL.match(string_input_uni_roll)
        if result is None:
            raise ValueError('Invalid University Roll')
        return input_uni_roll

    @validator('dept')
    def deptValidator(cls, input_dept):
        result = DEPT.match(input_dept)
        if result is None:
            raise ValueError('Invalid Dept. Use dept names as CSE/IT/ECE etc')
        return input_dept
    
    @validator('section')
    def sectionValidator(cls, input_section):
        string_input_section = str(input_section)

        result = SECTION.match(string_input_section)
        if result is None:
            raise ValueError('Invalid Section. Section only take 1 to 9')
        return input_section


# class Student(StudentBase):
#     class Config():
#         orm_mode = True
#         example={'name':'Kaushik Pal',
#                 'uni_roll':12000119098,
#                 dept:'CSE',
#                 section:2}


try:
    s = StudentBase(name='kaushik 12pal', uni_roll=120119098,
    dept='CSE', section=2)
    print("Successfully created student object")

    print(s)
except ValidationError as e:
    print(e.json())