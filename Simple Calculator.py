import math
import sys
def Simple_Calculator(): 

    choice = input("Enter an Operation (1/2/3/4/5/6/7) :")
    
    if choice == '7':
        print("Exiting the Simple Calculator.ByeBye")
        sys.exit()


    if choice in ('1','2','3','4','5','6'):
        num1 = float(input("Enter the first number :"))
        num2 = float(input("Enter the second number :"))

        print(f"You entered numbers : {num1},{num2}")
        
        # Arithmetic Operation
        if choice == '1':
            print(f" Result : {num1} + {num2} = { num1 + num2}")   # Addition Operation Occurs
        
        elif choice == '2':
            print(f" Result : {num1} - {num2} = {num1 - num2}")    # Subtraction Operation Occurs
        
        elif choice == '3':
            print(f" Result : {num1} * {num2} = {num1 * num2}")    # Multiplication Operation Occurs

        elif choice == '4':
            if num2 !=0:
                print(f" Result : {num1} / {num2} = {num1 / num2}")   # Division operation occurs when divisor not equals to zero
            
            else:
                print(" Error : Division Occur by zero")               #  Error occured when divisor equals to zero
            
        elif choice == '5':
            print(f" Result : {num1} ^ {num2} = {num1 ** num2}")       # Exponentiation Operation Occurs

        elif choice == '6':
            print(f" Result : {num1} % {num2} = {num1 % num2}")        # Modulus Operation Occurs

    else:
        print("Invalid Operation , please select a valid operation")   # Invalid choice

    
Simple_Calculator()

                  


