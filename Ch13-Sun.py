# File: Ch13-Sun.py
# Description: 
def main(two_D_list):
    if check(two_D_list):
        print("Lo Shu Magic Square")
    

def check(two_D_list):
    if vertical_test(two_D_list) == horizontal_test(two_D_list) and horizontal_test(two_D_list) == slanted_test(two_D_list):
        return True
    else:
        return False


def vertical_test(two_D_list):
    column_total = 0
    running_total = []
    for x in range(3):
        for elements in two_D_list:
            column_total += elements[x]
        running_total.append(column_total)
    return sum(running_total)


def horizontal_test(two_D_list):
    