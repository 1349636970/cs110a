# Filename: Ch04-Mon.py
# Description: Write a program that displays a table of the Celsius temperatures 0 through 20 and their Fahrenheit equivalents. The formula for converting a temperature from Celsius to Fahrenheit is

# F = 5/9 C + 32
# where F is the Fahrenheit temperature, and C is the Celsius temperature. Your program must use a loop to display the table.



print("\t|--------------------------------------------------------------------------|")
print("\t\tThe Celsius temperature","\tThe Fahrenheit temperature is")
print("\t|--------------------------------------------------------------------------|")
for x in range(21):
  print("\t\t\t",x,"\t\t\t\t",format((5/9)*x+32,'.2f'))
  print("\t|--------------------------------------------------------------------------|")

  
  
# [zlin79@hills cs110]$ python3 Ch04-Mon.py
#         |--------------------------------------------------------------------------|
#                 The Celsius temperature         The Fahrenheit temperature is
#         |--------------------------------------------------------------------------|
#                          0                               32.00
#         |--------------------------------------------------------------------------|
#                          1                               32.56
#         |--------------------------------------------------------------------------|
#                          2                               33.11
#         |--------------------------------------------------------------------------|
#                          3                               33.67
#         |--------------------------------------------------------------------------|
#                          4                               34.22
#         |--------------------------------------------------------------------------|
#                          5                               34.78
#         |--------------------------------------------------------------------------|
#                          6                               35.33
#         |--------------------------------------------------------------------------|
#                          7                               35.89
#         |--------------------------------------------------------------------------|
#                          8                               36.44
#         |--------------------------------------------------------------------------|
#                          9                               37.00
#         |--------------------------------------------------------------------------|
#                          10                              37.56
#         |--------------------------------------------------------------------------|
#                          11                              38.11
#         |--------------------------------------------------------------------------|
#                          12                              38.67
#         |--------------------------------------------------------------------------|
#                          13                              39.22
#         |--------------------------------------------------------------------------|
#                          14                              39.78
#         |--------------------------------------------------------------------------|
#                          15                              40.33
#         |--------------------------------------------------------------------------|
#                          16                              40.89
#         |--------------------------------------------------------------------------|
#                          17                              41.44
#         |--------------------------------------------------------------------------|
#                          18                              42.00
#         |--------------------------------------------------------------------------|
#                          19                              42.56
#         |--------------------------------------------------------------------------|
#                          20                              43.11
#         |--------------------------------------------------------------------------|
# [zlin79@hills cs110]$


