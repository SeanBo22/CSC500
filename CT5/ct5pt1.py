## Sean Bohuslavsky 
## CSC500 - Critical Thinking Assignment 5, Part 1
## Python Program to calculate the average rainfall per month

months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']

#Get rainfall for each month and print the number of months, total rainfall, and average rainfall per month
def rainfall(num_years):
    num = 0
    num_months = 0
    total_rainfall = 0
    while num < num_years:
        current_year = num + 1
        print("Year {}".format(current_year))
        for i in range(12):
            rainfall = int(input("Enter the inches of rainfall for {}: ".format(months[i])))
            num_months = num_months + 1
            total_rainfall = total_rainfall + rainfall
        num = num + 1
    
    average_rainfall = total_rainfall / num_months
    print("Total number of months: {}".format(num_months))
    print("Total Inches of rainfall: {}".format(total_rainfall))
    print("Average rainfall per month: {}".format(average_rainfall))

#Get user input
num_years = int(input("Enter the number of years: "))

#Call rainfall function
rainfall(num_years)