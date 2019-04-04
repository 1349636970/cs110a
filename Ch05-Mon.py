# Filename:Ch05-Mon.py
# Description: A nutritionist who works for a fitness club helps members by evaluating their diets. As part of her evaluation, she asks members for the number of fat grams and carbohydrate grams that they consumed in a day. Then, she calculates the number of calories that result from the fat, using the following formula:
# Calories from fat = fat grams x 9
# Next, she calculates the number of calories that result from the carbohydrates, using the following formula:
# Calories from carbs = carb grams x 4
# The nutritionist asks you to write a program that will make these calculations.


def main():
  fatGrams = float(input("the number of fat grams: "))
  carbGrams = float(input("the number of carb grams: "))
  print("the number of calories from the fat is",CaloriesFromFat(fatGrams))
  print("the number of calories from the  is carbohydrates",CaloriesFromCarbs(carbGrams))
  
def CaloriesFromFat(fatGrams):
  return fatGrams*9

def CaloriesFromCarbs(carbGrams):
  return carbGrams*4

main()

# [zlin79@hills cs110]$ python3 Ch05-Mon.py
# the number of fat grams: 10
# the number of carb grams: 20
# the number of calories from the fat is 90.0
# the number of calories from the  is carbohydrates 80.0
# [zlin79@hills cs110]$