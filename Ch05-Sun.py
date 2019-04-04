<<<<<<< HEAD
# Filename: Ch05-Sun.py
# Description: A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the actual value of a piece of property and displays the assessment value and property tax

ASSESSMENT_VALUE_PERCENT = 0.6
TAX = 0.72

def main():
    # Input
    property_value = askUser()
    # Calculation Process
    assessment_value = calculator(property_value,"assessment")
    property_tax = calculator(property_value,"tax")
    # Output
    displays(assessment_value,property_tax)

def askUser():
    return float(input("Enter your property value: "))
def calculator(operator,value_types):
    if value_types == "assessment":
        return operator*ASSESSMENT_VALUE_PERCENT
    elif value_types == "tax":
        return operator*ASSESSMENT_VALUE_PERCENT/100*TAX
    else:
        return "ERROR: value_types invalid"
def displays(assessment_value,property_tax):
    print("The assessment value is ",format(assessment_value,'.2f'),sep='$')
    print("The property tax is ",format(property_tax,'.2f'),sep="$")

main()

# [zlin79@hills cs110]$ python3 Ch05-Sun.py
# Enter your property value: 10000
# The assessment value is $6000.00
=======
# Filename: Ch05-Sun.py
# Description: A county collects property taxes on the assessment value of property, which is 60 percent of the property’s actual value. For example, if an acre of land is valued at $10,000, its assessment value is $6,000. The property tax is then 72¢ for each $100 of the assessment value. The tax for the acre assessed at $6,000 will be $43.20. Write a program that asks for the actual value of a piece of property and displays the assessment value and property tax

ASSESSMENT_VALUE_PERCENT = 0.6
TAX = 0.72

def main():
    # Input
    property_value = askUser()
    # Calculation Process
    assessment_value = calculator(property_value,"assessment")
    property_tax = calculator(property_value,"tax")
    # Output
    displays(assessment_value,property_tax)

def askUser():
    return float(input("Enter your property value: "))
def calculator(operator,value_types):
    if value_types == "assessment":
        return operator*ASSESSMENT_VALUE_PERCENT
    elif value_types == "tax":
        return operator*ASSESSMENT_VALUE_PERCENT/100*TAX
    else:
        return "ERROR: value_types invalid"
def displays(assessment_value,property_tax):
    print("The assessment value is ",format(assessment_value,'.2f'),sep='$')
    print("The property tax is ",format(property_tax,'.2f'),sep="$")

main()

# [zlin79@hills cs110]$ python3 Ch05-Sun.py
# Enter your property value: 10000
# The assessment value is $6000.00
>>>>>>> 7c4e499fbdaf271d5845bba69a8725f9c408aceb
# The property tax is $43.20