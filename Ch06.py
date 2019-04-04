# Assume a file containing a series of names (as strings) is named names.txt and exists on the computer’s disk. Write a program that displays the number of names that are stored in the file.
# (Hint: Open the file and read every string stored in it. Use a variable to keep a count of the number of items that are read from the file.)
def displays_names():
    f = open("names.txt",'r')
    # print(f.read())
    n=0
    for line in f:
        n+=1
    f.close()
    print(n)
# Assume a file containing a series of integers is named numbers.txtPreview the document and exists on the computer’s disk. Write a program that displays all of the numbers in the file.
def displays_numbers():
    file_input = open("numbers.txt",'r')
    print(file_input.read())
    file_input.close()

# Assume a file containing a series of integers is named numbers.txtPreview the document and exists on the computer’s disk. Write a program that calculates the average of all the numbers stored in the file.
def average_numbers():
    file_input = open("numbers.txt",'r')
    items = 0
    total = 0
    for line in file_input:
        total += int(line)
        items += 1
    file_input.close()
    print(total/items)

# Write a program that asks the user for the name of a file. The program should display the contents of the file with each line preceded with a line number followed by a colon. The line numbering should start at 1.
def display_line():
    file_name = input("Enter the file name: ")
    file_input = open(file_name,'r')
    n = 1
    for line in file_input:
        print(str(n)+":",line,end="")
        n+=1
    file_input.close()

# Assume a file containing a series of integers is named numbers.txtPreview the document and exists on the computer’s disk. Write a program that reads all of the numbers stored in the file and calculates their total.
def sum_of_numbers():
    file_input = open("numbers.txt",'r')
    print(int(file_input.read().strip("\n")))
    file_input.close()

sum_of_numbers()
