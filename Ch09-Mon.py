# Filename: Ch09-Mon.py
# Description: A software company sells a package that retails for $99. Quantity discounts are given according to the following table:

# Quantity	Discount
# 10–19	10%
# 20–49	20%
# 50–99	30%
# 100 or more	40%
# Write a program that asks the user to enter the number of packages purchased. The program should then display the amount of the discount (if any) and the total amount of the purchase after the discount.
def main():
    packages_purchased = float(input("Enter the number of packages purchased: "))
    if packages_purchased < 10:
        print("no discount",packages_purchased)
    if packages_purchased >= 10 and packages_purchased <= 19:
        print("discount: 10%")
        print("total amount of purchase",format(packages_purchased*0.1,'.2f'))
    elif packages_purchased >= 20 and packages_purchased <=49:
        print("discount: 20%")
        print("total amount of purchase",format(packages_purchased*0.2,'.2f'))
    elif packages_purchased >= 50 and packages_purchased <=99:
        print("discount: 30%")
        print("total amount of purchase",format(packages_purchased*0.3,'.2f'))
    else:
        print("discount: 40%")
        print("total amount of purchase",format(packages_purchased*0.4,'.2f'))
main()

# Enter the number of packages purchased: 100
# discount: 40%
# total amount of purchase 40.00