import random
# File: Ch13-Wed.py
# Description: 


def main():
    try:
        file_open = open("8_ball_responses.txt", 'r')
    except IOError as e:
        print(e)
    file_list = file_open.readlines()
    file_open.close()
    while (input("Enter your question: ") != "!q"):
        print(file_list[random.randint(0, len(file_list))])

main()