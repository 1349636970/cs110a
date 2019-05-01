from random import randint
# File: Ch15-Sun.py
# Description: Write a program that lets the user play the game of Rock, Paper, Scissors against the computer.

def main():
    game_choise = ['rock','paper','scissors']
    computer_choise = game_choise[randint(1,3)-1]
    user_answer = input('Enter your answer: ')
    result = 'computer win'
    if user_answer == computer_choise:
        result = 'play again'
    elif user_answer == 'rock':
        if computer_choise != 'paper':
            result = 'user win'
    elif user_answer == 'paper':
        if computer_choise != 'scissors':
            result = 'user win'
    elif user_answer == 'scissors':
        if computer_choise != 'rock':
            result = 'user win'
    return result

def test(result):
    while result == 'play again':
        print(result)
        result = main()
    print(result)

test(main())


# Enter your answer: rock
# play again
# Enter your answer: rock
# computer win