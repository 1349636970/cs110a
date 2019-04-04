# Filename: Ch02.py
# Description: This is a solution for Sales Tax problem in starting out with python

purchase = float(input("Enter purchase: "))
state_tax = purchase*0.04
county_tax = purchase*0.02
total_sales_tax = state_tax+county_tax
total_sales = purchase+total_sales_tax
print("Purchase: ",format(purchase,'.2f'),sep = "$")
print("State_tax: ",format(state_tax,'.2f'),sep = "$")
print("County_tax: ",format(county_tax,'.2f'),sep = "$")
print("Total Sales Tax: ",format(total_sales_tax,'.2f'),sep = "$")
print("Total Sale: ",format(total_sales,'.2f'),sep = "$")

# [zlin79@hills cs110]$ python3 Ch02.py
# Enter purchase: 200.25
# Purchase: $200.25
# State_tax: $8.01
# County_tax: $4.00
# Total Sales Tax: $12.02
# Total Sale: $212.26