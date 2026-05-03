'''
1. Program starts and displays a welcome message showing available operators: + - * / % ** sqrt
2. User is prompted to enter the first number
3. If the user types "exit" at any input stage, the program closes cleanly with a goodbye message
4. If the input is not a valid number, flag the error and ask again: do not proceed
5. User is prompted to enter an operator
6. If the operator is not one of the 7 allowed ones, flag the error and ask again
7. If the operator is sqrt, skip to Step 10 immediately
8. User is prompted to enter the second number
9. If the input is not a valid number, flag the error and ask again
10. If the operator is / or % and the second number is 0, flag a division by zero error and ask for the second number again
11. Program performs the calculation
12. Result is displayed in the format: firstNumber operator secondNumber = result
13. For sqrt the format is: √firstNumber = result
14. User is prompted: type new to calculate again or exit to quit
15. If new: return to Step 2 cleanly
16. If exit: close the program with a goodbye message
17. If anything else: flag it and show the prompt again
'''
'''
def welcomeToProgram():
    
    while True:
        
        welcome = input("Type 'op' to view menu or (Type 'exit' to exit the program): ")
        
        if welcome.lower() == "exit":
            print("Goodbye")
            break
        
        print("=============================")
        print("WELCOME TO THE CLI CALCULATOR")
        print("=============================")
        
        print("THE OPERATORS THAT CAN BE USED (+ - * / % ** sqrt) ")
    

def getUserInput():
    number1 = int(input("Enter the first number: "))
    if number1 > 0:
        print(f"Valid number entered: {number1}")
    else:
        print("Invalid number entered. Try again.")
    
welcomeToProgram()
# getUserInput()

'''

'''

CALCULATOR BOILERPLATE:

[TOP] 
- Define helper functions (add, sub, etc.)

[MIDDLE] 
- Create a main "run" function
    - Start 'while' loop
        - Get user input
        - Validate input (check for exit command)
        - Try:
            - Call logic functions
            - Display result
        - Except:
            - Show error message
            - Loop continues

[BOTTOM]
- Call the main "run" function
'''
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
        print("Select an operator to continue / type 'exit' to exit the program")
        choice = input("Enter the operator you wish to use or exit to leave the program: ").lower()
        
        if choice == "exit":
            print("Good...Bye")
            break
        
        #if choice in ('+', '-', '*', '/', '**', '%', 'sqrt'):
        if choice == "sqrt":
            
            
            try:
                # This is where the user input will be received
                num1 = float(input("Enter the first number: "))
                math.sqrt(num1)
                print(math.sqrt(num1))
            except ValueError:
                print("Invalid Number inserted. Enter a valid number to continue.")
                
        else:
            
            try:
                
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                # This is where the if statements will be placed based on the choice of operator the user wishes to utilize
                if choice == "+":
                    print(f"The result of  {num1} + {num2}: {addition(num1, num2)}")
                elif choice == "-":
                    print(f"The result of  {num1} - {num2}: {subtraction(num1, num2)}")
                elif choice == "*":
                    print(f"The result of  {num1} * {num2}: {multiplication(num1, num2)}")
                elif choice == "/":
                    print(f"The result of  {num1} / {num2}: {division(num1, num2)}")
                elif choice == "**":
                    print(f"The result of the power of {num1}: {power(num1, num2)}")
                elif choice == "%":
                    print(f"The result of modulus {num1}: {modulus(num1, num2)}")
            except ValueError:
                print("Invalid Number inserted. Enter a valid number to continue.")


runCalculator()

