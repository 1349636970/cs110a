# Filename: Ch10-Mon.py
# Description: In mathematics, the notation n! represents the factorial of the nonnegative integer n. The factorial of n is the product of all the nonnegative integers from 1 to n. For example,

# and

# Write a program that lets the user enter a nonnegative integer then uses a loop to calculate the factorial of that number. Display the factorial.
def main():
    integer = int(input("Enter a positive integer: "))
    factorial = 1
    for x in range(integer,0,-1):
        factorial *= x
    print("factorial:",factorial)
main()

# Enter a positive integer: 3
# factorial: 6
