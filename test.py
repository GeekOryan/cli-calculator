# input() function practice
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2

print(f"The sum of {num1} and {num2} is: {sum}")

'''

'''
Learning areas for this CLI Calculator:
input() Function
float() conversion
if/elif/else
while loops
try/except
functions
math module
'''

'''
Thoroughly Completed learning areas: 
input() function
float() conversion
'''

# float() conversion
'''
numberVariable = "24"

conversion = float(numberVariable)
print(conversion)

'''

'''
My Learnings:
So in order to convert a different data type to another of which in this instance was a string to a float.
Two different Variables are required so that the string will be associated to that variable and the float function will be
allocated to the second variable.
Previously I made the error of merely naming one variable then calling the float function with the string inside the brackets 
like this: 
numberVariable = "24"
float(numberVariable)
print(float()) or print(float)

This was the incorrect way to do it.
'''

'''
numVariable = 24

print(type(numVariable))
floatConversion = float(numVariable)
print(floatConversion)
'''


# IF/ELIF/ELSE STATEMENTS

# An if statement based on a grade checker

'''
mark = 82

if mark >= 80:
    print("Distinction")
elif mark >= 70:
    print("Merit")
elif mark >= 50:
    print("Passed")
else:
    print("Failed")
'''

# WHILE LOOPS
'''

x = 1

while x <= 10:
    print(x)
    x += 1

'''
'''
My Learnings:

So we start by initializing, create a variable and allocate a starting point from where the loop should start from.
Then the code says while the variable is less than a set number, the contents of that variable must be printed over and over again.
then the x += 1 means that it will increase the count of the program till it reaches the set number.

So there are 2 ways of getting something done, something as in printing 10 numbers for example.
If I wanted to print exactly 10 numbers I will type: x = 1 and then while x < 11: print(x) x += 1
The other way to print exactly 10 numbers will be x = 1 and then while x <= 10: print(x) x += 1

These two code will produce the same output. 
Of course there is a third way of which is by setting the initialization to 0, but I do not think that is good practice. 
I mean it could even depend on the program.
'''

# New Year Countdown Loop

'''
x = 10

while x >= 1:
    print(x)
    x -= 1
    

message = "HAPPY NEW YEAR"
print(message)

'''

'''
My learnings:

In this New Year Countdown Clock.

I began by initializing from 10, as that is where I wanted to start the countdown from (10).
Then the program will only run if x is greater or equal to 1.
Then the count will decrease by 1 as I intend on counting backwards due to the nature of the program (New year countdown)


The program broke at some stage though I set initialization to 10, then while x > 1: print(x) x += 1

I then realized it was because of the count, it had to be set at -= and not += as I would be counting upwards 
Of which is the direct opposite of what I intended to do.

'''


'''
x = 10

while x > 1:
    print(x)
    x += 1
    

message = "HAPPY NEW YEAR"
print(message)
'''

# A while loop with a break statement.

'''

x = 1

while x < 11:
    print(x)
    if x == 8:
        break
    x += 1
    
'''


# Try/Except Error Handling.
'''
try:
    print(x)
except:
    print("An exception occurred")
    
x = -2

if x < 0:
    raise Exception("Apologies, no negative numbers are allowed.")

try:
    print(y)
except NameError:
    print("The Variable y has not been defined.")
except:
    print("Something else went wrong.")
    
    
'''

'''
As I was learning this concept I noticed that except cannot be used in the same block of code more than once.
If the except keyword is to be used in the same block of code twice, one of them must be given a key variable of some sort
Like ValueError or NameError or even Exception (Maybe).

Maybe the Exception can only be used for the raise keyword.

Oh they are not called key variables they are called built in exceptions.
There are a lot more than the Value and Name ones
'''

# FUNCTIONS

def myFunction():
    print("Hello Universe")
    
myFunction()

# A Temperature conversion calculator using a function.

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(60))
print(fahrenheit_to_celsius(82))
print(fahrenheit_to_celsius(98))

def calculateSum(num1, num2):
    return num1 + num2

print(calculateSum(22, 24))

def calculateDifference(num1, num2):
    return num1 - num2

print(calculateDifference(24, 16))

def calculateQuotient(num1, num2):
    return num1 - num2

print(calculateQuotient(18, 6))

def calculateMultiplication(num1, num2):
    return num1 * num2

print(calculateMultiplication(72, 3))



# Math Module

x = min(10, 24, 98)
y = max(1000, 12, 12344)

print(x)
print(y)

# The abs() function returns the absolute (positive) value of the specified number:

x = abs(-16.25)

print(x)

# The power function pow(x, y)

x = pow(4, 3)

print(x)

# The Math Module

import math


x = math.sqrt(64)

print(x)