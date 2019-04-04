# When a bank account pays compound interest, it pays interest not only on the principal amount that was deposited into the account, but also on the interest that has accumulated over time. Suppose you want to deposit some money into a savings account, and let the account earn compound interest for a certain number of years. The formula for calculating the balance of the account after a specified number of years is:

# LaTeX: A = P\left(1 +\frac{r}{n}\right) ^ {nt} A = P(1 + r n) n t

# The terms in the formula are:

# A is the amount of money in the account after the specified number of years.

# P is the principal amount that was originally deposited into the account.

# r is the annual interest rate.

# n is the number of times per year that the interest is compounded.

# t is the specified number of years.

# Write a program that makes the calculation for you. The program should ask the user to input the following:

# The amount of principal originally deposited into the account

# The annual interest rate paid by the account

# The number of times per year that the interest is compounded(For example, if interest is compounded monthly, enter 12. If interest is compounded quarterly, enter 4.)

# The number of years the account will be left to earn interest

# Once the input data has been entered, the program should calculate and display the amount of money that will be in the account after the specified number of years.

# The user should enter the interest rate as a percentage. For example, 2 percent would be entered as 2, not as .02. The program will then have to divide the input by 100 to move the decimal point to the correct position.

def main():
    formula_argument = ask_user()
    if formula_argument is None:
        print("Program End")
    else:
        amount_money = calculation(formula_argument)
        display(amount_money)


def ask_user():
    amount_of_principal = input("The amount of principal originally deposited into the account: ")
    annual_interest_rate = input("The annual interest rate paid by the account: ")
    number_of_times_per_year = input("""The number of times per year that the interest is compounded (For example, if interest is compounded monthly, enter 12. If interest is compounded quarterly, enter 4.): """)
    number_of_years_left = input("The number of years the account will be left to earn interest: ")
    verify_int_result = verify_int_variable([annual_interest_rate, number_of_times_per_year, number_of_years_left])
    verify_float_result = verify_float_variable([amount_of_principal])
    if verify_int_result is False or verify_float_result is False:
        return None
    else:
        return {"amount_of_principal": float(amount_of_principal), "annual_interest_rate": int(annual_interest_rate)/100, "number_of_times_per_year": int(number_of_times_per_year), "number_of_years_left": int(number_of_years_left)}


def verify_float_variable(variable_float_list):
    verify_false_result = []
    verify_true_result = []
    for variable in variable_float_list:
        try:
            float(variable)
        except:
            print("Measure everything you type only contain number, no any symbol")
            verify_false_result.append(False)
        else:
            verify_true_result.append(int(variable))
    if False in verify_false_result:
        return False


def verify_int_variable(variable_int_list):
    verify_false_result = []
    verify_true_result = []
    for variable in variable_int_list:
        try:
            int(variable)
        except:
            print("Measure everything you type only contain number, no any symbol")
            verify_false_result.append(False)
        else:
            verify_true_result.append(int(variable))
    if False in verify_false_result:
        return False

def calculation(formula_argument):
    amount_of_principal = formula_argument["amount_of_principal"]
    annual_interest_rate = formula_argument["annual_interest_rate"]
    number_of_times_per_year = formula_argument["number_of_times_per_year"]
    number_of_years_left = formula_argument["number_of_years_left"]

    return amount_of_principal*(1+(annual_interest_rate/number_of_times_per_year))**(number_of_times_per_year*number_of_years_left)


def display(amount_money):
    print(amount_money)


main()
