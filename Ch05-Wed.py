# Filename: Ch05-Web.py
# Description: Programming Exercise 8: A painting company has determined that for every 112 square feet of wall space, one gallon of paint and eight hours of labor will be required. The company charges $35.00 per hour for labor. Write a program that asks the user to enter the square feet of wall space to be painted and the price of the paint per gallon. The program should display the following data:

# The number of gallons of paint required
# The hours of labor required
# The cost of the paint
# The labor charges
# The total cost of the paint job
# This assignment covers the material in chapter 5. Key topics are:

# try/except/else/finally
# open/close a file
# read/write/readline a file
# looping to read a file

def main():
#   Input
  spaceOfWall = wallSpace()
  Paintprice = pricePaint()
#   process
  gallonsOfPaint = quantity(spaceOfWall,"paint")
  hoursOfLabor = quantity(spaceOfWall,"labor")
  paintCost = gallonsOfPaint*Paintprice
  laborCharges = hoursOfLabor*35
  total = laborCharges+paintCost
#   result
  print("The number of gallons of paint required:",gallonsOfPaint)
  print("The hours of labor required:",hoursOfLabor)
  print("The cost of the paint:",paintCost)
  print("The labor charges:",laborCharges)
  print("The total cost of the paint job:",total)
  
  
def wallSpace():
  return float(input("Enter the square feet of wall space to be painted: "))
def pricePaint():
  return float(input("Enter the price of the paint per gallon: "))


def quantity(wallSpace,category):
  if category == "paint":
    return wallSpace/112
  elif category == "labor":
    return wallSpace/8
  else:
    return "error"
main()

# [zlin79@hills cs110]$ python3 Ch05-Wed.py
# Enter the square feet of wall space to be painted: 224
# Enter the price of the paint per gallon: 10
# The number of gallons of paint required: 2.0
# The hours of labor required: 28.0
# The cost of the paint: 20.0
# The labor charges: 980.0
# The total cost of the paint job: 1000.0
# [zlin79@hills cs110]$ ^C