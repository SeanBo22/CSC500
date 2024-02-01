## Sean Bohuslavsky 
## CSC500 - Critical Thinking Assignment 3, Part 2
## Python Program to calculate when alarm clock with go off

# Function to print hour an alarm will go off given current time and time between
def alarm(current_time, time_between):
    if time_between > 24:
        hours = time_between % 24
        hours = current_time + hours
    else:
        hours = current_time + time_between
    if hours > 24:
        hours = hours - 24
    print("Your alarm will go off at: {}".format(hours))

# Get user input
current_time = int(input("Enter the current time (24 hour time): "))
time_between = int(input("Enter the number of hours to wait for the alarm: "))

# Call function
alarm(current_time, time_between)