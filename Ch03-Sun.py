# Filename: Ch03.py
# Description: Write a program that asks the user to enter an object’s mass, then calculates its weight. If the object weighs more than 500 newtons, display a message indicating that it is too heavy. If the object weighs less than 100 newtons, display a message indicating that it is too light.
# weight = mass x 9.8
mass = float(input("Enter an object's mass: "))
if mass > 500:
  print('Too heavy')
elif mass < 100:
  print('Too light')
else:
  print("weight is",format(mass*9.8,'.2f'))
# [zlin79@hills ~]$ cd cs110/
# [zlin79@hills cs110]$ python3 Ch03.py
# Enter an object's mass: 20
# Too light
# [zlin79@hills cs110]$ python3 Ch03.py
# Enter an object's mass: 1100
# Too heavy
# [zlin79@hills cs110]$ python3 Ch03.py
# Enter an object's mass: 600
# Too heavy
# [zlin79@hills cs110]$ python3 Ch03.py
# Enter an object's mass: 200
# weight is 1960.00
# [zlin79@hills cs110]$