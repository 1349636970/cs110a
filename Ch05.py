# Write a program that asks the user to enter the monthly costs for the following expenses incurred from operating his or her automobile: loan payment, insurance, gas, oil, tires, and maintenance. The program should then display the total monthly cost of these expenses, and the total annual cost of these expenses.

def automobileCosts():
  loadPayment = float(input("Enter loan payment for month: "))
  gas = float(input("Enter gas: "))
  oil = float(input("Enter oil: "))
  tires = float(input("Enter tires: "))
  insurance = float(input("Enter insurance: "))
  maintenance = float(input("Enter maintenance: "))
  monthCost = totalMonthlyCost(loadPayment,gas,oil,tires,insurance,maintenance)
  print(monthCost)
  print(totalAnnualCost(monthCost))

def totalMonthlyCost(loadPayment,gas,oil,tires,insurance,maintenance):
  return loadPayment+gas+oil+tires+insurance+maintenance

def totalAnnualCost(totalMonthlyCost):
  return totalMonthlyCost*12
  
  
# Write a program that asks the user to enter a distance in kilometers, then converts that distance to miles. The conversion formula is as follows:

# Miles = kilometers x 0.6214
def kilometerConverter():
  kilometers = float(input("Enter a distance in kilometers: "))
  miles = kilometerConverterFormula(kilometers)
  print(format(miles,'.2f'))
  
def kilometerConverterFormula(kilometers):
  miles = kilometers*0.6214
  return miles
kilometerConverter()


# Many financial experts advise that property owners should insure their homes or buildings for at least 80 percent of the amount it would cost to replace the structure. Write a program that asks the user to enter the replacement cost of a building, then displays the minimum amount of insurance he or she should buy for the property.

def insurance():
  replacementCost = float(input("Enter the replacement cost of a building: "))
  print(replacementCost*0.8)








