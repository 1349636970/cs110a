# At one college, the tuition for a full-time student is $8, 000 per semester. It has been announced that the tuition will increase by 3 percent each year for the next 5 years. Write a program with a loop that displays the projected semester tuition amount for the next 5 years.

# TUITION_START = 8000
# INCREASE_PERCENT = 0.03
# def main():
#     tution = TUITION_START
#     for year in range(5):
#         tution *= (1+INCREASE_PERCENT)
#     print(tution)
# main()


# Write a program that calculates the amount of money a person would earn over a period of time if his or her salary is one penny the first day, two pennies the second day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, then show the total pay at the end of the period. The output should be displayed in a dollar amount, not the number of pennies

# PENNIES_VALUE = 0.01

# PAY_PER_DAY_INCREASE = 2

# def main():
#     pay_per_day_start = 1
#     period_day = int(input("Enter days: "))
#     total_pennies = 0
#     print("\tDay\t", "Salary")
#     for x in range(1, period_day+1):

#         total_pennies += pay_per_day_start
#         pay_per_day_start = pay_per_day_start * PAY_PER_DAY_INCREASE

#         print(format(x, '10'), format(total_pennies*PENNIES_VALUE, '11.2f'))
#     total_dollar = total_pennies*PENNIES_VALUE
#     print("total", format(total_dollar, '.2f'))


# main()


# Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an application that displays the number of millimeters that the ocean will have risen each year for the next 25 years.

RISING = 1.6
YEARS = 25
def main():
    risen = 0
    for year in range(YEARS):
        risen+=RISING
        print(risen)
main()