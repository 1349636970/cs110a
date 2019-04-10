import random
# File: Ch12.py
# Description: Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold.


# def main():
#     generation_status = generation_random(check_input())
#     if (generation_status):
#         print("Generation success")
#     else:
#         print(generation_status)


# def check_input():
#     quantity_random_number = None
#     while quantity_random_number is None:
#         try:
#             quantity_random_number = int(input("Please tell me how many ramdon number you want: "))
#             if quantity_random_number < 0:
#                 print("Please Enter a positive number")
#                 quantity_random_number = None
#         except:
#             print("Please Enter a positive number")
#     if quantity_random_number is not None:
#         return quantity_random_number

# def generation_random(quantity_random_number):
#     try:
#         file_name = open("random_number", 'w')
#         for x in range(quantity_random_number):
#             file_name.write(str(random.randint(1, 501))+"\n")
#         file_name.close()
#     except Exception as e:
#         return (e)
#     else:
#         return True

# Modify the program that you wrote for Chapter 6, Exercise 6 so it handles the following exceptions:
# It should handle any IOError exceptions that are raised when the file is opened and data is read from it.
# It should handle any ValueError exceptions that are raised when the items that are read from the file are converted to a number.

def main():
    total = 0
    count = 0
    try:
        file_input = open('numbers.txt', 'r')

        for line in file_input:
            total += int(line)
            count += 1

        file_input.close()

        print('average', total/count)
    except IOError as err:
        print('file not found')
    except ValueError as error:
        print("value error")

    return True


main()
# Write a program that asks the user for the name of a file. The program should display only the first five lines of the file’s contents. If the file contains less than five lines, it should display the file’s entire contents.
main()
