## Sean Bohuslavsky 
## CSC500 - Critical Thinking Assignment 5, Part 2
## Python Program to calculate students reward points

#Set points_awarded based on num_books
def points(num_books):
    if num_books >=0 and num_books <= 1:
        points_awarded = 0
    elif num_books > 1 and num_books <= 3:
        points_awarded = 5
    elif num_books > 3 and num_books <= 5:
        points_awarded = 15
    elif num_books > 5 and num_books <= 7:
        points_awarded = 30
    elif num_books > 7:
        points_awarded = 60
    return points_awarded

#Get user input
num_books = int(input("Enter the number of books you have purchased this month: "))

#Call points function
points_rewarded = points(num_books)
print("You have earned {} points this month".format(points_rewarded))