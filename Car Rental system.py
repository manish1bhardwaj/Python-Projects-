# 5. Problem: Car Rental System 
# Description: Develop a Car class for a rental system, including attributes like model, color, 
# and methods for calculating rental charges. 


class Car:
    def __init__(self, model, color, base_rate):   
        self.model = model
        self.color = color
        self.base_rate = base_rate
    def calculate_rental_charge(self, days, discount=0):       
        if days < 0:
            raise ValueError("Number of days cannot be negative.")       
        daily_rate = self.base_rate * (1 - discount)
        total_cost = days * daily_rate
        return total_cost
    def __str__(self):
        return f"Car Model: {self.model}, Color: {self.color}, Base Rate: {self.base_rate}"

# Example Usage
car1 = Car("Toyota Corolla", "Blue", 40)
print(car1)
print("Rental Charge for 5 days:", car1.calculate_rental_charge(5))
print("Rental Charge for 5 days with 10% discount:", car1.calculate_rental_charge(5,0.1))