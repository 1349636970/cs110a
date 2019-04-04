# Filename: Ch03.py
# Description: Write a program that asks the user to enter an object’s mass, then calculates its weight. If the object weighs more than 500 newtons, display a message indicating that it is too heavy. If the object weighs less than 100 newtons, display a message indicating that it is too light.
# weight = mass x 9.8
def homework():
  mass = float(input("Enter an object's mass: "))
  if mass > 500:
    print('Too heavy')
  elif mass < 100:
    print('Too light')
  else:
    print("weight is",format(mass*9.8,'.2f'))
homework()
# Write a program that asks the user to enter a person’s age. The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult. Following are the guidelines:
# If the person is 1 year old or less, he or she is an infant.
# If the person is older than 1 year, but younger than 13 years, he or she is a child.
# If the person is at least 13 years old, but less than 20 years old, he or she is a teenager.
# If the person is at least 20 years old, he or she is an adult.    
def classwork():
  age = float(input("Enter your age: "))
  print("He/She is an")
  if age <= 1:
    print("infant")
  elif age < 13:
    print("child")
  elif age < 20:
    print("teenager")    
  else:
    print("adult")
    
    



def classwork1():
  # Filename:Ch03.py  
  # Description: Assume hot dogs come in packages of 10, and hot dog buns come in packages of 8. Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog buns needed for a cookout, with the minimum amount of leftovers. The program should ask the user for the number of people attending the cookout and the number of hot dogs each person will be given. The program should display the following details:

  # The minimum number of packages of hot dogs required

  # The minimum number of packages of hot dog buns required

  # The number of hot dogs that will be left over

  # The number of hot dog buns that will be left over
  
  
  people = int(input("Enter people: "))
  hotDogs = int(input("Enter how many hot dogs each person eat: "))
  minimumHotDogs = people*hotDogs
  minimumHotDogsBuns = minimumHotDogs
  hotDogsPackages = minimumHotDogs//10
  if minimumHotDogs % 10 != 0:
    hotDogsPackages += 1
  hotDogsBunsPackages = minimumHotDogsBuns//8
  if minimumHotDogsBuns % 8 != 0:
    hotDogsBunsPackages += 1
  leftHotDogs = hotDogsPackages * 10 - minimumHotDogs
  leftHotDogsBuns = hotDogsBunsPackages * 8 - minimumHotDogsBuns
  print("The minimum number of packages of hot dogs required:",hotDogsPackages,'packages')
  print("The minimum number of packages of hot dog buns required",hotDogsBunsPackages,'packages')
  print("The number of hot dogs that will be left over",leftHotDogs)
  print("The number of hot dog buns that will be left over",leftHotDogsBuns)
  
  
  # [zlin79@hills cs110]$ python3 Ch03.py
  # Enter people: 7
  # Enter how many hot dogs each person eat: 3
  # The minimum number of packages of hot dogs required: 3 packages
  # The minimum number of packages of hot dog buns required 3 packages
  # The number of hot dogs that will be left over 9
  # The number of hot dog buns that will be left over 3
# classwork1()
    
    
    
    
    
    
    
    
    
