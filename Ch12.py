import random
# File: Ch12.py
# Description: Write a program that writes a series of random numbers to a file. Each random number should be in the range of 1 through 500. The application should let the user specify how many random numbers the file will hold.


def main():
    generation_status = generation_random(check_input())
    if (generation_status):
        print("Generation success")
    else:
        print(generation_status)


def check_input():
    quantity_random_number = None
    while quantity_random_number is None:
        try:
            quantity_random_number = int(input("Please tell me how many ramdon number you want: "))
            if quantity_random_number < 0:
                print("Please Enter a positive number")
                quantity_random_number = None
        except:
            print("Please Enter a positive number")
    if quantity_random_number is not None:
        return quantity_random_number

def generation_random(quantity_random_number):
    try:
        file_name = open("random_number", 'w')
        for x in range(quantity_random_number):
            file_name.write(str(random.randint(1, 501))+"\n")
        file_name.close()
    except Exception as e:
        return (e)
    else:
        return True


main()
