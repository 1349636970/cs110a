# File: Ch12-Wed.py
# Description: Write a program that asks the user for the name of a file. The program should display only the first five lines of the file’s contents. If the file contains less than five lines, it should display the file’s entire contents.

def main():
    filename_input = input("Please Enter a filename: ")
    try:
        file_open = open(filename_input, 'r')
    except Exception as e:
        print(e)
    else:
        file_list = file_open.readlines()
        file_open.close()
        if len(file_list) >= 5:
            print(file_list[:5])
        else:
            print(file_open.read())
main()
