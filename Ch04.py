# Write a program that asks the user to enter the amount that he or she has budgeted for a month. A loop should then prompt the user to enter each of his or her expenses for the month and keep a running total. When the loop finishes, the program should display the amount that the user is over or under budget.

def classwork1():
  result = 0
  budgeted = int(input("Enter your budgeted: "))
  expenses = 1
  while expenses != 0:
    expenses = int(input("Enter your expenses: "))
    result+=expenses #result = result+expense
  if result > budgeted:
    print("You are over budget")
  else:
    print("You are under budget")
classwork1()

    