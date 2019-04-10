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
        if len(file_list) >= 5:
            for line in file_list[:5]:
                print(line,end="")
        else:
            for line in file_list:
                print(line,end="")
        file_open.close()
main()

# Please Enter a filename: steps.txt
# 374
# 36
# 258
# 306
# 234
