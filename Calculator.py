# 1. Problem: Calculator 
# Description: Create a simple calculator class that can perform basic arithmetic operations 
# (addition, subtraction, multiplication, division).

class Calculator: 
    def __init__(self): 
        pass

    def add(self, num1, num2): 
        return num1 + num2 
    def subtract(self, num1, num2): 
        return num1 - num2 
    def multiply(self, num1, num2): 
        return num1 * num2 
    def divide(self, num1, num2): 
        if num2 != 0: 
            return num1 / num2 
        else: 
            return "Error: Division by zero." 
# Example Usage: 
calc = Calculator() 
print("Addition:", calc.add(5, 3)) 
print("Subtraction:", calc.subtract(8, 2)) 
print("Multiplication:", calc.multiply(4, 6)) 
print("Division:", calc.divide(10, 2))