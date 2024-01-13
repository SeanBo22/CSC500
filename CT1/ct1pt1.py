## Sean Bohuslavsky 
## CSC500 - Critical Thinking Assignment 1, Part 1
## Python Program to add and subtract two numbers

# Add two numbers and print result
def add(num1, num2):
    sum = num1 + num2
    print("Sum: {}".format(sum))

# Subtract two numbers and print result
def sub(num1, num2):
    dif = num1 - num2
    print("Difference: {}".format(dif))

# Get user input
num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))

# Call functions
add(num1, num2)
sub(num1, num2)