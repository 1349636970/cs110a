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
        print(file_list[random.randint(0, len(file_list)-1)])

main()

# Enter your question:
# Probably not

# Enter your question:
# Maybe

# Enter your question:
# Most likely no

# Enter your question:
# Definitely no
# Enter your question:
# Most definitely yes

# Enter your question:
# As I see it, yes

# Enter your question:
# Perhaps

# Enter your question:
# Yes

# Enter your question:
# For sure

# Enter your question:
# As I see it, yes
