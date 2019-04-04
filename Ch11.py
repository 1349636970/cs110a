# File: Ch11.py
# Description: One foot equals 12 inches. Write a function named feet_to_inches that accepts a number of feet as an argument and returns the number of inches in that many feet. Use the function in a program that prompts the user to enter a number of feet then displays the number of inches in that many feet.


# def main():
#     input_feet = verify_input()
#     inches = feet_to_inches(input_feet)
#     display(inches)


# def feet_to_inches(input_feet):
#     return input_feet*12


# def display(inches):
#     print("result:", inches)


# def verify_input():
#     input_feet = None
#     while(input_feet is None):
#         try:
#             input_feet = float(input("Please input feet: "))
#         except:
#             print("Please Enter feet")
#         else:
#             if input_feet < 0:
#                 print("Please Enter a positive number")
#                 input_feet = None
#     if input_feet is not None:
#         return input_feet
# def main():
#     countClassATicketsSold = getClassATicketsSold()
#     countClassBTicketsSold = getClassBTicketsSold()
#     countClassCTicketsSold = getClassCTicketsSold()
#     totalSale = calcTotalSale(countClassATicketsSold,countClassBTicketsSold, countClassCTicketsSold)
#     displayTotalSales(totalSale)
#     return True


# def getClassATicketsSold():
#     return int(input("Enter seat of Class A: "))*CLASSACOST


# def getClassBTicketsSold():
#     return int(input("Enter seat of Class A: "))*CLASSBCOST


# def getClassCTicketsSold():
#     return int(input("Enter seat of Class A: "))*CLASSCCOST


# def calcTotalSale(countClassATicketsSold, countClassBTicketsSold, countClassCTicketsSold):
#     return countClassATicketsSold+countClassBTicketsSold+countClassCTicketsSold


# def displayTotalSales(totalSale):
#     print("Total sales: ", totalSale,end="$")

# def main():
#     ticketClassSales = []
#     for ticketClass in ['A','B','C']:
#         ticketClassSales.append(getClassATicketsSold(ticketClass))
#     totalSale = calcTotalSale(ticketClassSales)
#     displayTotalSales(totalSale)


# def getClassATicketsSold(ticketClass):
#     if ticketClass == "A":
#         return int(input("Enter seat of Class "+ticketClass+": "))*CLASSACOST
#     if ticketClass == "B":
#         return int(input("Enter seat of Class "+ticketClass+": "))*CLASSBCOST
#     if ticketClass == "C":
#         return int(input("Enter seat of Class "+ticketClass+": "))*CLASSCCOST


# def calcTotalSale(ticketClassSales):
#     return sum(ticketClassSales)


# def displayTotalSales(totalSale):
#     print("Total sales: ", totalSale, sep="$")


# A retail company must file a monthly sales tax report listing the total sales for the month, and the amount of state and county sales tax collected. The state sales tax rate is 5 percent and the county sales tax rate is 2.5 percent. Write a program that asks the user to enter the total sales for the month. From this figure, the application should calculate and display the following:

# The amount of county sales tax
# The amount of state sales tax
# The total sales tax(county plus state)
def main():
    input_sales = sales_input()
    state_tax = calculation_tax(input_sales, 5)
    county_tax = calculation_tax(input_sales, 2.5)
    print("state tax is", state_tax)
    print("county tax is", county_tax)
    print("total sale tax is",state_tax+county_tax)


def sales_input():
    input_sales = None
    while (input_sales is None):
        try:
            input_sales = float(input("Enter your sales: "))
            if input_sales < 0:
                print("Please Enter positive number")
                input_sales = None
        except:
            print("Please Enter positive number")
    if input_sales is not None:
        return input_sales


def calculation_tax(input_sales,tax_rate):
    tax_rate /= 100
    return input_sales*tax_rate


main()
