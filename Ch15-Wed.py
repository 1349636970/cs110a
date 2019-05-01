from random import randint
import sys
# File: Ch15-Wed.py
# Description: Write a program that generates a random number in the range of 1 through 100, and asks the user to guess what the number is. If the user’s guess is higher than the random number, the program should display “Too high, try again.” If the user’s guess is lower than the random number, the program should display “Too low, try again.” If the user guesses the number, the application should congratulate the user and generate a new random number so the game can start over.

def main():
    rant = randint(1,100)
    user_answer = None
    count = 0
    while user_answer is None:
        user_answer = input("Guess a number(press !q exit): ")
        if user_answer != '!q':    
            user_answer = int(user_answer)    
            if user_answer > rant:
                print("too heigh, try again")
                count += 1
            elif user_answer < rant:
                print("too low, try again")
                count += 1
            else:
                print('congratulation, you win! Do one more!')
                print('Guess number:',count)
                count = 0
                rant = randint(1,100)
            user_answer = None
main()

# Guess a number(press !q exit): 20
# too low, try again
# Guess a number(press !q exit): 30
# too low, try again
# Guess a number(press !q exit): 40
# too low, try again
# Guess a number(press !q exit): 50
# too low, try again
# Guess a number(press !q exit): 60
# too heigh, try again
# Guess a number(press !q exit): 52
# too heigh, try again
# Guess a number(press !q exit): 51
# congratulation, you win! Do one more!
# Guess number: 6
# Guess a number(press !q exit): 