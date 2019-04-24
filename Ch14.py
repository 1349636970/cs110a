# File: Ch14.py
# Description: 
def main():
    weight = float(input("Enter your package weight: "))
    if weight > 10:
        rate = 4.75
    elif weight > 6:
        rate = 4.00
    elif weight > 2:
        rate = 3.00
    elif weight > 0:
        rate = 1.50
    charges = weight * rate
    print(charges)
main()