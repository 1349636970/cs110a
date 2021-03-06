# Filename: Ch09-Web.py
# Description: Write a program that calculates and displays a person’s body mass index(BMI). The BMI is often used to determine whether a person is overweight or underweight for his or her height. A person’s BMI is calculated with the following formula:

# LaTeX: BMI\: =\: weight\: \times\frac{703}{height ^ 2} B M I = w e i g h t × 703 h e i g h t 2
# where weight is measured in pounds and height is measured in inches. The program should ask the user to enter his or her weight and height, then display the user’s BMI. The program should also display a message indicating whether the person has optimal weight, is underweight, or is overweight. A person’s weight is considered to be optimal if his or her BMI is between 18.5 and 25. If the BMI is less than 18.5, the person is considered to be underweight. If the BMI value is greater than 25, the person is considered to be overweight.

def main():
    user_weight = float(input("Enter you weight: "))
    user_height = float(input("Enter you height: "))
    BMI = user_weight*(703/(user_height**2))
    if BMI < 0:
        print("ERROR")
    else:
        if BMI > 25:
            person_weight = "overweight"
        elif BMI >18.5:
            person_weight = "optimal"
        else:
            person_weight = "underweight"
        print(person_weight)
    
main()
# Enter you weight: 130
# Enter you height: 6
# overweight
