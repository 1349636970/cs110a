# GirlNames.txt Preview the documentThis file contains a list of the 200 most popular names given to girls born in the United States from the year 2000 through 2009.

# BoyNames.txtPreview the document This file contains a list of the 200 most popular names given to boys born in the United States from the year 2000 through 2009.

# Write a program that filereads the contents of the two files into two separate lists. The user should be able to enter a boy’s name, a girl’s name, or both, and the application will display messages indicating whether the names were among the most popular.

def main():
    user_input = ask_user()
    verify_user_input = verify(user_input)
    display(verify_user_input)


def ask_user():
    return input("Enter names: ")


def verify(user_input):
    boy_name = boy_names()
    girl_name = girl_names()
    if user_input in boy_name or user_input in girl_name:
        return True
    else:
        return False

def boy_names():
    boy_names_list = []
    try:
        boy_names = open("boyNames.txt", 'r')
        for boy_name in boy_names:
            boy_names_list.append(boy_name.strip("\n"))
    except IOError as error:
        print("File not exist")
        print(error)
    else:
        boy_names.close()    
    return boy_names_list


def girl_names():
    girl_names_list = []
    try:
        girl_names = open("girlNames.txt", 'r')
        for girl_name in girl_names:
            girl_names_list.append(girl_name.strip('\n'))
    except IOError as error:
        print("file not exist")
        print(error)
    else:
        girl_names.close()
    return girl_names_list


def display(status):
    if status:
        print("Your name is popular")
    else:
        print("Your name is not popular")


main()

# [zlin79@hills cs110]$ python3 Ch07-Wed.py
# Enter names: 1
# Your name is not popular
# [zlin79@hills cs110]$ python3 Ch07-Wed.py
# Enter names: Samantha
# Your name is popular
# [zlin79@hills cs110]$
