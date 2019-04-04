# Filename: Ch04-Sun
# Description: Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. The program should first ask for the number of years. The outer loop will iterate once for each year. The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user for the inches of rainfall for that month. After all iterations, the program should display the number of months, the total inches of rainfall, and the average rainfall per month for the entire period.

years = int(input("Please enter number of years you want to calculate: "))
totalRainfall = 0
numberOfMonths = 0
for year in range(1,years+1):
  for month in range(1,13):
    months = float(input("Please enter #"+str(year)+" year"+" #"+str(month)+" month data: "))
    totalRainfall += months
    numberOfMonths += 1
    if month == 12 and year != years:
      print("#",year," year is finish, now continue enter #",year+1," year data",sep = "")
print("number of months is",numberOfMonths,)
print("total inches of rainfall is",totalRainfall)
print("the average rainfall per month for the entire period is",format(totalRainfall/numberOfMonths,'.2f'))

# [zlin79@hills cs110]$ python3 Ch04-Sun.py
# Please enter number of years you want to calculate: 2
# Please enter #1 month data: 1
# Please enter #2 month data: 2
# Please enter #3 month data: 3
# Please enter #4 month data: 4
# Please enter #5 month data: 5
# Please enter #6 month data: 6
# Please enter #7 month data: 7
# Please enter #8 month data: 8
# Please enter #9 month data: 9
# Please enter #10 month data: 10
# Please enter #11 month data: 11
# Please enter #12 month data: 12
# #1 is finish, now continue enter #2 data
# Please enter #1 month data: 1
# Please enter #2 month data: 2
# Please enter #3 month data: 3
# Please enter #4 month data: 4
# Please enter #5 month data: 5
# Please enter #6 month data: 6
# Please enter #7 month data: 7
# Please enter #8 month data: 8
# Please enter #9 month data: 9
# Please enter #10 month data: 10
# Please enter #11 month data: 11
# Please enter #12 month data: 12
# number of months is 24
# total inches of rainfall is 156.0
# the average rainfall per month for the entire period is 6.50
      