# 3. Problem: Employee Management System 
# Description: Design an Employee class with attributes like name, employee ID, and 
# methods for calculating salary based on hours worked. 




class Employee:
    def __init__(self,name,employee_id,hourly_rates):
        self.name=name
        self.employee_id=employee_id
        self.hourly_rates=hourly_rates
    def salaryCalculator(self,hours_worked):
        return hours_worked*self.hourly_rates
    def getDetails(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Hourly Rate: {self.hourly_rate}"
Employee=Employee("Manish Bhardwaj", 3457, 1000.0)
hours_worked = 160 
salary = Employee.salaryCalculator(hours_worked)

print(f"Name : {Employee.name} \nID: {Employee.employee_id}\nSalary: Rs.{salary}")