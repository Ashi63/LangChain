from pydantic import BaseModel,EmailStr,Field
from typing import Optional

# basic example
class Student(BaseModel):
    name:str
    
new_student = {'name': 'ashish'}

student1 = Student(**new_student)

print("Basic Example:",student1)
print(type(student1))

# default value
class Student(BaseModel):
    name: str = 'Ashish'
    
new_student = {}

student = Student(**new_student)

print('Default Value:',student)

# Optional Value

class Student(BaseModel):
    name: str = 'Ashish'
    age: Optional[int] = None
    
new_student = {}
student = Student(**new_student)

print(student)

# type coerce
class Student(BaseModel):
    name: str = 'Ashish'
    age: Optional[int] = None
    
new_student = {'age':'1'}
student = Student(**new_student)

print(student)

# Validations example email
class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    
new_student = {'name':'Ashish','age':37,'email':'abc@gmail.com'}
student = Student(**new_student)

print(student)

# Field function (constraints,default values, description, regex, expressions) 
class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0,lt=10,default=1,description='A decimal value representing the cgpa')                        )
    
new_student = {'name':'Ashish','age':37,'email':'abc@gmail.com','cgpa':8}
student = Student(**new_student)

print(student)


