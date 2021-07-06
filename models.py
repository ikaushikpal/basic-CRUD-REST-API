from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base
from CONST import *
class StudentDB(Base):
    __tablename__ = 'students'

    uni_roll = Column(Integer, primary_key=True, index=True, autoincrement=True, nullable=False)
    name = Column(String(MAX_NAME_LENGTH), nullable=False)
    dept = Column(String(MAX_DEPT_LENGTH), nullable=False)
    section = Column(Integer, nullable=False)
