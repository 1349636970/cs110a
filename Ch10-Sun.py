# Filename: Ch10-Sun.py
# Description: If a moderately active person cuts their calorie intake by 500 calories a day, they can typically lose about 4 pounds a month. Write a program that lets the user enter their starting weight, then creates and displays a table showing what their expected weight will be at the end of each month for the next 6 months if they stay on this diet.

MONTHS = 6
def main():
    start_weight = None
    while start_weight is None:
        try:
            start_weight = float(input("Enter your weight: "))
            if start_weight <= 0:
                print("Please Enter you real weight!")
                start_weight = None
        except:
            print("Please Enter a number")
    print("\tmonth\t","weight")
    for month in range(1,MONTHS+1):
        start_weight -= 4
        if start_weight >= 0:
            print(format(month, '10'), format(start_weight, "12.2f"))
main()

# Enter your weight: 23
# month    weight
# 1        19.00
# 2        15.00
# 3        11.00
# 4         7.00
# 5         3.00
