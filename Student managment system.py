# 2. Problem: Student Management System 
# Description: Implement a Student class with attributes like name, roll number, and 
# methods for displaying student details.


class Student:
    def __init__(self,name,roll_no,course,branch):
        self.name=name
        self.roll_no=roll_no
        self.course=course
        self.branch=branch
    def getDetails(self):
        print(f'''Name : {self.name}\nRoll No. : {self.roll_no}\nCourse : {self.course}\nBranch : {self.branch}''')
Student1 = Student("Manish Bhardwaj","29","B-Tech","CSE(AIML & IOT)")
Student1.getDetails()