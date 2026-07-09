# Lab 1: Pure vs Impure functions
#Reference: CSC3301

# Pure Functions
def square(x):
    return  x * x

print("square of 4:", square(4))  # Output: 16

# Impure Functions
import random
def roll():
    return random.randint(1, 6)

print("Dice roll:", roll())