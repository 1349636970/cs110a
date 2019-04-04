# Filename:Ch08-Sun.py

# Description: Write a program that asks the user for the number of males and the number of females registered in a class. The program should display the percentage of males and females in the class.

# Hint: Suppose there are 8 males and 12 females in a class. There are 20 students in the class. The percentage of males can be calculated as 8 ÷ 20 = 0.4, or 40 % . The percentage of females can be calculated as 12 ÷ 20 = 0.6, or 60 % .
def main():
    number_people = ask_user()
    percentage = calculation(number_people)
    display(percentage)


def ask_user():
    males = int(input("Enter number of males: "))
    females = int(input("Enter number of females: "))
    return [males,females]


def calculation(number_people):
    percentage_males = number_people[0]/sum(number_people)
    percentage_females = number_people[1]/sum(number_people)
    return [percentage_males,percentage_females]


def display(percentage):
    print("males",format(percentage[0],'.2%'))
    print("females", format(percentage[1], '.2%'))


main()

# Enter number of males: 10
# Enter number of females: 10
# males 50.00%
# females 50.00%