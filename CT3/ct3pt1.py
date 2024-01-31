## Sean Bohuslavsky 
## CSC500 - Critical Thinking Assignment 3, Part 1
## Python Program to calculate restaurant bill

# Function to calculate tip, tax, and total when given an initial cost
def bill(cost):
    tip = (cost * 18) * .01
    tax = (cost * 7) * .01
    total = cost + tip + tax
    print("Bill: Initial Cost    Tip    Tax   Total Cost")
    print("      ${}           ${}  ${}  ${}".format(cost, tip, tax, total))

#Get user input
cost = float(input("Enter Cost: "))

#Call bill function
bill(cost)