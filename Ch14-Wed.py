# File: Ch14-Wed.py
# Description: You have a group of friends coming to visit for your high school reunion, and you want to take them out to eat at a local restaurant. You aren’t sure if any of them have dietary restrictions, but your restaurant choices are as follows:

# Joe’s Gourmet Burgers—Vegetarian: No, Vegan: No, Gluten-Free: No

# Main Street Pizza Company—Vegetarian: Yes, Vegan: No, Gluten-Free: Yes

# Corner Café—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes

# Mama’s Fine Italian—Vegetarian: Yes, Vegan: No, Gluten-Free: No

# The Chef’s Kitchen—Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes

# Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-free, to which then displays only the restaurants to which you may take the group.

# Here is an example of the program’s output:

# Is anyone in your party a vegetarian? yes 
# Is anyone in your party a vegan? no 
# Is anyone in your party gluten-free? yes 
# Here are your restaurant choices:
# Main Street Pizza Company
# Corner Cafe
# The Chef's Kitchen
# Here is another example of the program’s output:

# Is anyone in your party a vegetarian? yes 
# Is anyone in your party a vegan? yes 
# Is anyone in your party gluten-free? yes 
# Here are your restaurant choices:
# Corner Cafe
# The Chef's Kitchen

def init():
    answer_list = []
    restaurant_list = []
    restaurant_list.append(["Joe’s Gourmet Burgers",[False,False,False]])
    restaurant_list.append(["Main Street Pizza Company",[True,False,True]])
    restaurant_list.append(["Corner Café",[True,True,True]])
    restaurant_list.append(["Mama’s Fine Italian",[True,False,False]])
    restaurant_list.append(["The Chef’s Kitchen",[True,True,True]])
    while (len(answer_list)!=3):
        is_vegetarian = input("Is anyone in your party a vegetarian? ")
        is_vegan = input("Is anyone in your party a vegan? ")
        is_gluten_free = input("Is anyone in your party gluten-free? ")
        for item in [is_vegetarian,is_vegan,is_gluten_free]:
            if item == "yes":
                answer_list.append(True)
            elif item == "no":
                answer_list.append(False)
        if len(answer_list) != 3:
            print("Please only type in yes or no")
            answer_list = []
    main(answer_list,restaurant_list)

def main(answer_list,restaurant_list):
    restaurant_name = 0
    restaurant_boolean = 1
    choise = []
    count = 0
    is_loop_done = 0
    for answer in range(len(answer_list)):
        
        for restaurant in restaurant_list:
            count += 1
            if answer_list[answer] is False:
                choise.append(restaurant)
            elif answer_list[answer] == restaurant[restaurant_boolean][answer]:
                choise.append(restaurant)
            if count == len(restaurant_list):
                restaurant_list = choise
                if is_loop_done != len(answer_list)-1:
                    choise = []
                count = 0
        is_loop_done += 1
        
                

    for x in choise:
        print(x[restaurant_name])


init()

# Is anyone in your party a vegetarian? yes
# Is anyone in your party a vegan? no
# Is anyone in your party gluten-free? yes
# Main Street Pizza Company
# Corner Café
# The Chef’s Kitchen