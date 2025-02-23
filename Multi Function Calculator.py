# Multi Function Calculator

import math

# Arithmetic Operation
def add(*nums):
    return sum(nums)

def subtract(x, *nums):
    return x - sum(nums)

def multiply(*nums):
    from math import prod  # Using Python's built-in product function
    return prod(nums)
    
def divide(x, *nums):
    for num in nums:
        if num == 0:
            return "Error ! Division by zero."
        x /= num   # Direct division 
        return x
   
# Power & Root Operation
def power(x, *nums):
    for num in nums:
        x **= num
    return x

def sqrt(x):
    if x < 0:
        return "Error! Square root of a negative number."
    return math.sqrt(x)

# Logarithmic Operation
def log(x, base=10):
    if x <= 0:
        return "Error! Logarithm of non-positive number."
    return math.log(x, base)

# Trigonometric Operation
def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    if cos(x) == 0:
        return "Error! Tangent undefined at this angle."
    return math.tan(math.radians(x))

def cosec(x):
    if sin(x) == 0:
        return "Error! Cosecant undefined at this angle."
    return 1 / sin(x)

def sec(x):
    if cos(x) == 0:
        return "Error! Secant undefined at this angle."
    return 1 / cos(x)

def cot(x):
    if tan(x) == 0:
        return "Error! Cotangent undefined at this angle."
    return 1 / tan(x)

def calculator():
    
    choice = input("Choose an operation (1-13): ")
    
    if choice in ['1', '2', '3', '4', '5']:
        numbers = list(map(float, input("Enter numbers separated by space: ").split()))
        
        if not numbers:
            print("Error! No numbers provided.")
            return
        
        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide,
            '5': power
        }
        print("Result:", operations[choice](*numbers))
    
    elif choice == '6':
       numbers = input("Enter a single number: ").split()
       if len(numbers) != 1:
          print("Error! Please enter only one number.")
          return 
       x = float(numbers[0])
       print("Result:", sqrt(x))

    
    elif choice == '7':
        x = float(input("Enter a number: "))
        base = float(input("Enter base (default 10): ") or 10)
        print("Result:", log(x, base))
    
    elif choice in ['8', '9', '10', '11', '12', '13']:
        x = float(input("Enter angle in degrees: "))
        trig_operations = {
            '8': sin,
            '9': cos,
            '10': tan,
            '11': cosec,
            '12': sec,
            '13': cot
        }
        print("Result:", trig_operations[choice](x))
    
    else:
        print("Invalid choice! Please select a valid operation.")

if __name__ == "__main__":
    calculator()
