import math


def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error: Division by Zero"
    else:
        return num1 / num2
    
def power(num1, num2):
    return pow(num1, num2)

def modulus(num1, num2):
    return num1 % num2

def sqrt(num1):
    return math.sqrt(num1)
        

def runCalculator():
    print("=============================")
    print("WELCOME TO THE CLI CALCULATOR")
    print("=============================")
        
    print("THE OPERATORS THAT CAN BE USED (+ - * / % ** sqrt) ")
    
    while True:
        choice = input("Enter the operator you wish to use or exit to leave the program: ").lower()
        
        if choice == "exit":
            print("Good...Bye")
            break
        
        if choice == "sqrt":
            
            
            try:
                # This is where the user input will be received
                num1 = input("Enter the first number: ")
                if num1 == "exit":
                    break
                    
                float_value = float(num1)
                math.sqrt(float_value)
                print(f"√{float_value} = {math.sqrt(float_value)}")
                
                newExitInput = input("Type 'new' to calculate again or 'exit' to quit the program: ")
                if newExitInput == "exit":
                    print("Good...Bye")
                    break
                else:
                    continue
            except ValueError:
                print("Invalid Number inserted. Enter a valid number to continue.")
                
        else:
            
            try:
                
                num1 = input("Enter the first number: ")
                if num1 == "exit":
                    break
                
                num2 = input("Enter the second number: ")
                if num2 == "exit":
                    break
                
                float_value = float(num1)
                float_value2 = float(num2)
                # This is where the if statements will be placed based on the choice of operator the user wishes to utilize
                if choice == "+":
                    print(f"The result of {float_value} + {float_value2} = {addition(float_value, float_value2)}")
                elif choice == "-":
                    print(f"The result of {float_value} - {float_value2} = {subtraction(float_value, float_value2)}")
                elif choice == "*":
                    print(f"The result of {float_value} * {float_value2} = {multiplication(float_value, float_value2)}")
                elif choice == "/":
                    print(f"The result of {float_value} / {float_value2} = {division(float_value, float_value2)}")
                elif choice == "**":
                    print(f"The result of the power of {float_value} = {power(float_value, float_value2)}")
                elif choice == "%":
                    print(f"The result of modulus {float_value} = {modulus(float_value, float_value2)}")
                else:
                    print(f"The operator {choice} you selected is invalid. Try again.")
                    
                
                newExitInput = input("Type 'new' to calculate again or 'exit' to quit the program: ")
                if newExitInput == "exit":
                    print("Good...Bye")
                    break
                else:
                    continue
                
            except ValueError:
                print("Invalid Number inserted. Enter a valid number to continue.")


runCalculator()