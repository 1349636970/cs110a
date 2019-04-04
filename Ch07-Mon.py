# Filename: Ch07-Mon.py
# In a program, write a function that accepts two arguments: a list, and a number n. Assume that the list contains numbers. The function should display all of the numbers in the list that are greater than the number n.

def main(list_input,number):
    print("These number is greaten than",number)
    for element in list_input:
        if element > number:
            print(element)
main([1,2,3,4,5,6,7,8],3)

# [zlin79@hills cs110]$ python3 Ch07-Mon.py
# These number is greaten than 3
# 4
# 5
# 6
# 7
# 8
# [zlin79@hills cs110]$
