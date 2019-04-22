from math import sqrt
# File: Ch13.py
# Description: A positive integer greater than 1 is said to be prime if it has no divisors other than 1 and itself. A positive integer greater than 1 is composite if it is not prime. Write a program that asks the user to enter an integer greater than 1, then displays all of the prime numbers that are less than or equal to the number entered. The program should work as follows:

# Once the user has entered a number, the program should populate a list with all of the integers from 2 up through the value entered.
# The program should then use a loop to step through the list. The loop should pass each element to a function that displays the element whether it is a prime number.


def main():
    positive_numbers = range(2,int(input("Please give me a positive integer number: ")))
    prime = []
    for prime_number in positive_numbers:
        if check_primary(prime_number):
            prime.append(prime_number)
    print(prime)
    
def check_primary(number):
    number_status = True
    for x in range(2,number):
        if number % x == 0:
            number_status = False
    return number_status
    
main()
