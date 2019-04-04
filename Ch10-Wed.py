# Filename:Ch10-Wed.py

# Description: Write a program that uses nested loops to draw this pattern:

# *******
# ******
# *****
# ****
# ***
# **
# *



def main():
    total_lines = 7
    star_number = 7
    for line in range(total_lines):
        for star in range(star_number):
            print("*",end="")
        star_number -= 1
        print("\n",end="")

main()

# *******
# ******
# *****
# ****
# ***
# **
# *
