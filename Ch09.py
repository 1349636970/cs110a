# Create a change-counting game that gets the user to enter the number of coins required to make exactly one dollar. The program should prompt the user to enter the number of pennies, nickels, dimes, and quarters. If the total value of the coins entered is equal to one dollar, the program should congratulate the user for winning the game. Otherwise, the program should display a message indicating whether the amount entered was more than or less than one dollar.


# coin_value = [0.01,0.05,0.1,0.25]
# coin_name = ["pennies", "nickels", 'dimes', 'quarters']

# def main():
#     money = ask_user()
#     result = calculation(money)
#     display(result)

# def ask_user():
#     coin_list = []
    
#     for x in range(4):
#         coin_list.append(int(input("Enter "+coin_name[x]+": ")))
#     return coin_list

# def calculation(money):
#     money_total = 0
#     for number_coin in range(len(money)):
#         money_total += money[number_coin]*coin_value[number_coin]
#     if money_total > 1:
#         return "more than 1 dollar"
#     elif money_total == 1:
#         return "You win the game"
#     else:
#         return "less than 1 dollar"

# def display(result):
#     print(result)


# The colors red, blue, and yellow are known as the primary colors because they cannot be made by mixing other colors. When you mix two primary colors, you get a secondary color, as shown here:

# When you mix red and blue, you get purple.

# When you mix red and yellow, you get orange.

# When you mix blue and yellow, you get green.

# Design a program that prompts the user to enter the names of two primary colors to mix. If the user enters anything other than “red, ” “blue, ” or “yellow, ” the program should display an error message. Otherwise, the program should display the name of the secondary color that results.

# LIST_COLOR = [["red", "blue", "purple"], ["red","yellow","orange"],["blue","yellow","green"]]
# PRIMARY_COLOR = ["red",'blue','yellow']
# def main():
#     color = ask_user()
#     if not color:
#         print("Only type in red, blue and yellow")
#     else:
#         mix_result = mix(color)
#         display(mix_result)


# def ask_user():
#     first_color = input("Enter first color: ")
#     second_color = input("Enter second color: ")
#     if verify(first_color, second_color):
#         return [first_color,second_color]
#     else:
#         return False

# def verify(first_color, second_color):
#     if first_color not in PRIMARY_COLOR:
#         return False
#     elif second_color not in PRIMARY_COLOR:
#         return False
#     else:
#         return True

# def mix(color_input):
#     for x in LIST_COLOR:
#         if color_input[0] in x and color_input[1] in x:
#             return x[2]

# def display(result):
#     print(result)



# main()


# On a roulette wheel, the pockets are numbered from 0 to 36. The colors of the pockets are as follows:

# Pocket 0 is green.
# For pockets 1 through 10, the odd-numbered pockets are red and the even-numbered pockets are black.
# For pockets 11 through 18, the odd-numbered pockets are black and the even-numbered pockets are red.
# For pockets 19 through 28, the odd-numbered pockets are red and the even-numbered pockets are black.
# For pockets 29 through 36, the odd-numbered pockets are black and the even-numbered pockets are red.
# Write a program that asks the user to enter a pocket number and displays whether the pocket is green, red, or black. The program should display an error message if the user enters a number that is outside the range of 0 through 36.

def main():
    # pocket_number = int(input("Enter a pocket number: "))
    # pocket_range = [[1,10,"red","black"],[11,18,"black","red"],[19,28,"red","black"],[29,36,"black","red"]]
    # if pocket_number == 0:
    #     pocket_default_color = "green"
    # if pocket_number > 36 or pocket_number < 0:
    #     pocket_default_color = "ERROR"
    # else:
    #     for x in pocket_range:
    #         if pocket_number in range(x[0]+1,x[1]+1,2):
    #             pocket_default_color = x[3]
    #         elif pocket_number in range(x[0],x[1]+1,2):
    #             pocket_default_color = x[2]
    # print(pocket_default_color)
    pocket_number = int(input("Enter a pocket Number: "))
    if pocket_number > 36 or pocket_number < 0:
        pocket_color = "ERROR"
    elif pocket_number >= 29:
        if pocket_number % 2 != 0:
            pocket_color = "black"
        else:
            pocket_color = "red"
    elif pocket_number >= 19:
        if pocket_number % 2 != 0:
            pocket_color = "red"
        else:
            pocket_color = "black"
    elif pocket_number >= 11:
        if pocket_number % 2 != 0:
            pocket_color = "black"
        else:
            pocket_color = "red"
    elif pocket_number >= 1:
        if pocket_number % 2 != 0:
            pocket_color = "red"
        else:
            pocket_color = "black"
    else:
        pocket_color = "green"
    print(pocket_color)
main()
