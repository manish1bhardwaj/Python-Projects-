# 9. Problem: Dice Simulator 
# Description: Develop a Dice class that simulates rolling a six-sided die

import random

class Dice:
    def roll(self):
        return random.randint(1, 6)

# Example Usage
dice = Dice()
roll_result = dice.roll()
print(f"Rolled a {roll_result}")