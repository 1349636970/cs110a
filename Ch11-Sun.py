import random
# File: Ch11-Sun.py
# Description: Write a program that gives simple math quizzes. The program should display two random numbers that are to be added, such as:

#   247
# + 129
# The program should allow the student to enter the answer. If the answer is correct, a message of congratulations should be displayed. If the answer is incorrect, a message showing the correct answer should be displayed.


def init():
    init_random_numbers = generator_random_number(2)
    main(init_random_numbers)


def main(init_random_numbers):
    input_answer = answer_input(init_random_numbers)
    answer_verify = verify(input_answer, init_random_numbers)
    display(answer_verify, init_random_numbers)


def generator_random_number(number_quantity):
    random_numbers = []
    for rand in range(number_quantity):
        random_numbers.append(random.randrange(1, 1000))
    return random_numbers


def answer_input(random_numbers):
    print("Your question is ")
    for random_number in random_numbers:
        if random_numbers.index(random_number) != 0:
            print("+", random_number)
        else:
            print(" ", random_number)
    user_input = None
    while(user_input is None):
        try:
            user_input = int(input("Please Enter your answer: "))
        except:
            print("Please Enter number")
    if user_input is not None:
        return user_input


def verify(input_answer, init_random_numbers):
    if input_answer == sum(init_random_numbers):
        return True
    else:
        return False


def display(result, init_random_numbers):
    if result:
        print("correct")
    else:
        print("incorrect, do you want to try again?(Y/N) ",end="")
        if input() == "Y":
            main(init_random_numbers)


init()


# Your question is
#   959
# + 854
# Please Enter your answer: 1813
# correct