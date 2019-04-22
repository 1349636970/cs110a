# File: Ch14.py
# Description: 
def main():
    month_input = input("Enter a year: ")
    if month_input % 100 == 0:
        if month_input % 400 == 0:
            print(month_input,"has 29 day")
        else:
            print(month_input,"has 28 day")
    else:
        if month_input % 4 == 0:
            print(month_input,"has 29 day")
        else:
            print(month_input,"has 28 day")    