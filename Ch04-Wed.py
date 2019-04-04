# Filename: Ch04-Web.py
# Description: Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative number to signal the end of the series. After all the positive numbers have been entered, the program should display their sum.

result = 0
order = 1
positiveNumber = int(input("Enter a positiveNumber #"+str(order)+": "))
while positiveNumber >= 0:
  order+=1
  result+=positiveNumber
  positiveNumber = int(input("Enter a positiveNumber #"+str(order)+": "))
print(result)


# [zlin79@hills cs110]$ python3 Ch04-Wed.py
# Enter a positiveNumber: 1
# Enter a positiveNumber: 2
# Enter a positiveNumber: 3
# Enter a positiveNumber: 4
# Enter a positiveNumber: 5
# Enter a positiveNumber: 6
# Enter a positiveNumber: 7
# Enter a positiveNumber: 8
# Enter a positiveNumber: 9
# Enter a positiveNumber: 10
# Enter a positiveNumber: -1
# 55