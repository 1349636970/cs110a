# File: Ch13-Sun.py
# Description: 
def main(two_D_list):
    vertical_number = vertical_test(two_D_list)
    horizontal_number = horizontal_test(two_D_list)
    slanted_number = slanted_test(two_D_list)
    if vertical_number == horizontal_number and horizontal_number == slanted_number:
        print("Shu Magic Square") 
    else:
        print("not Shu Magic Square") 


def vertical_test(two_D_list):
    column_total = 0
    running_total = []
    count = 0
    for x in range(3):
        for elements in two_D_list:
            column_total += elements[x]
        running_total.append(column_total)
    for item in range(1,len(running_total)):
        if running_total[item-1] == running_total[item]:
            count += 1
    if count == 3:
        return running_total[0]

def horizontal_test(two_D_list):
    column_total = 0
    running_total = []
    count = 0
    for x in range(3):
        for elements in two_D_list:
            running_total.append(sum(elements))
        running_total.append(column_total)
    for item in range(1,len(running_total)):
        if running_total[item-1] == running_total[item]:
            count += 1
    if count == 3:
        return running_total[0]
    
def slanted_test(two_D_list):
    column_total = 0
    running_total = []
    count = 0
    for elements in range(len(two_D_list)):
        column_total+=two_D_list[elements][elements]
    running_total.append(column_total)
    for elements in range(len(two_D_list)-1,0,-1):
        column_total+=two_D_list[elements][count]
        count+=1
    running_total.append(column_total)
    if running_total[0] == running_total[1]:
        return running_total[0]

main([[4,9,2],[3,5,7],[8,1,6]])

# Shu Magic Square
