# Filename:Ch03-Web.py  
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