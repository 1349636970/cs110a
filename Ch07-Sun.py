# FileName: Ch07-Sun.py

# Use the file charge_accounts.txtPreview the document in the Chapter 07 folder. This file has a list of a company’s valid charge account numbers. Each account number is a seven-digit number, such as 5658845.

# Write a program that reads the contents of the file into a list. The program should then ask the user to enter a charge account number. The program should determine whether the number is valid by searching for it in the list. If the number is in the list, the program should display a message indicating the number is valid. If the number is not in the list, the program should display a message indicating the number is invalid.

def main():
    input_account_number = ask_user()
    verify_result = verify_account(input_account_number)
    display(verify_result)

def ask_user():
    return input("Enter your account number: ")

def verify_account(input_account_number):
    charge_accounts_list = file_open()
    if input_account_number in charge_accounts_list:
        return True
    elif len(charge_accounts_list) == 0:
        return None
    else:
        return False

def file_open():
    charge_accounts_list = []
    try:
        charge_accounts_file = open("charge_accounts.txt",'r')
    except IOError:
        print("File doesn't exist")
    else:
        for charge_account in charge_accounts_file:
            charge_accounts_list.append(charge_account.strip('\n'))
        charge_accounts_file.close()
    return charge_accounts_list

def display(verify_result):
    if verify_result:
        print("The number is valid")
    elif verify_result is None:
        print(verify_result)
    else:
        print("The number is not valid")

main()

# [zlin79@hills cs110]$ python3 Ch07-Sun.py
# Enter your account number: 8354512
# The number is valid
# [zlin79@hills cs110]$ python3 Ch07-Sun.py
# Enter your account number: 123
# The number is not valid
# [zlin79@hills cs110]$ python3 Ch07-Sun.py
# Enter your account number: 123
# File doesn't exist
# None