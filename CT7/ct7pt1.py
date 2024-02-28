## Sean Bohuslavsky 
## CSC500 - Critical Thinking Assignment 5, Part 2
## Python Program to get room number, instructor, and meeting time based on course number.

#Dictionaries
room_number = {'CSC101':3004, 'CSC102':4501, 'CSC103':6755, 'NET110':1244, 'COM241':1411}
instructor = {'CSC101':'Haynes', 'CSC102':'Alvarado', 'CSC103':'Rich', 'NET110':'Burke', 'COM241':'Lee'}
meeting_time = {'CSC101':'8:00 a.m.', 'CSC102':'9:00 a.m.', 'CSC103':'10:00 a.m.', 'NET110':'11:00 a.m.', 'COM241':'1:00 p.m.'}

#Values function
def values(course_number):
    print("Here is the following information for course {}".format(course_number))
    print("Course room number: {}".format(room_number[course_number]))
    print("Course instructor: {}".format(instructor[course_number]))
    print("Course meeting time: {}".format(meeting_time[course_number]))

#Get user input
course_number = input("Enter a course number: ")
values(course_number)