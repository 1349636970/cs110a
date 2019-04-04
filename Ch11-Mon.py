# File: Ch11-Mon.py
# Description: Write a function named "max" that accepts two integer values as arguments and returns the value that is the greater of the two. For example, if 7 and 12 are passed as arguments to the function, the function should return 12. Use the function in a program that prompts the user to enter two integer values. The program should display the value that is the greater of the two.


def main():
    input__first_integer = integer_input("first")
    input__second_integer = integer_input("second")
    greater_compare = compare_greater(input__first_integer, input__second_integer)
    display(greater_compare)


def integer_input(order):
    input_integer = None
    while (input_integer is None):
        try:
            input_integer = int(input("Please Enter an "+order+" integer: "))
        except:
            print("Please an integer")
    if input_integer is not None:
        return input_integer


def compare_greater(input__first_integer, input__second_integer):
    if input__first_integer == input__second_integer:
        return "Two number are the same"
    elif input__first_integer < input__second_integer:
        return input__second_integer
    else:
        return input__first_integer


def display(result):
    print("This number is greater: ", result)

main()


# Please Enter an first integer: 1
# Please Enter an second integer: 2
# This number is greater:  2
