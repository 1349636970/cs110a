# Filename: Ch08-Mon.py

# Description: Last month, Joe purchased some stock in Acme Software, Inc. Here are the details of the purchase:

# The number of shares that Joe purchased was 2, 000.

# When Joe purchased the stock, he paid $40.00 per share.

# Joe paid his stockbroker a commission that amounted to 3 percent of the amount he paid for the stock.

# Two weeks later, Joe sold the stock. Here are the details of the sale:

# The number of shares that Joe sold was 2, 000.

# He sold the stock for $42.75 per share.

# He paid his stockbroker another commission that amounted to 3 percent of the amount he received for the stock.

# Write a program that displays the following information:

# The amount of money Joe paid for the stock.

# The amount of commission Joe paid his broker when he bought the stock.

# The amount for which Joe sold the stock.

# The amount of commission Joe paid his broker when he sold the stock.

# Display the amount of money that Joe had left when he sold the stock and paid his broker(both times). If this amount is positive, then Joe made a profit. If the amount is negative, then Joe lost money.

SHARES = 2000
PURCHASED_PER_SHARE = 40.00
SOLD_PER_SHARE = 42.75
COMMISSION = 0.03


def main():
    profit_info = calculation()
    display(profit_info)


def calculation():
    amount_money_paid_stock = SHARES * PURCHASED_PER_SHARE
    amount_commission_bought_stock = amount_money_paid_stock * COMMISSION
    amount_money_sold_stock = SOLD_PER_SHARE * SHARES
    amount_commission_sold_stock = amount_money_sold_stock * COMMISSION
    return [amount_money_paid_stock, amount_commission_bought_stock, amount_money_sold_stock, amount_commission_sold_stock]


def display(profit_info):
    print("The amount of money Joe paid for the stock:", format(profit_info[0], '.2f'))
    print("The amount of commission Joe paid his broker when he bought the stock:", format(profit_info[1], '.2f'))
    print("The amount for which Joe sold the stock", format(profit_info[2], '.2f'))
    print("The amount of commission Joe paid his broker when he sold the stock", format(profit_info[3], '.2f'))
    if verify_positive(profit_info):
        print("Joe made a profit")
    else:
        print("Joe lost money")


def verify_positive(profit_info):
    if (profit_info[2] - profit_info[3]) - (profit_info[1] + profit_info[0]) >= 0:
        return True
    else:
        return False


main()

# The amount of money Joe paid for the stock: 80000.00
# The amount of commission Joe paid his broker when he bought the stock: 2400.00
# The amount for which Joe sold the stock 85500.00
# The amount of commission Joe paid his broker when he sold the stock 2565.00
# Joe made a profit
