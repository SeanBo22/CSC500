## Sean Bohuslavsky 
## CSC500 - Critical Thinking Assignment 1, Part 2
## Python Program to multiply and divide two numbers

# Multiply two numbers and print result
def mul(num1, num2):
    prod = num1 * num2
    print("Product: {}".format(prod))

# Divide two numbers and print result
def div(num1, num2):
    quot = num1 / num2
    print("Quotient: {}".format(quot))

# Get user input
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

# Call functions
mul(num1, num2)
div(num1, num2)