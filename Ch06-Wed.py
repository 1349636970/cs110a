# File name: Ch06-Wed.py
# Description:Assume a file containing a series of integers is named numbers.txtPreview the document and exists on the computer’s disk. Write a program that reads all of the numbers stored in the file and calculates their total. Display the total.


file_input = open("numbers.txt",'r')
total = 0
for line in file_input:
    total += int(line)
file_input.close()
print(total)

# [zlin79@hills cs110]$ python3 Ch06-Wed.py
# 5421
# [zlin79@hills cs110]$