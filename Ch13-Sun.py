# File: Ch13-Sun.py
# Description: 
def main(two_D_list):
    running_total = 0
    for element in two_D_list:
        running_total += sum(element)
        if running_total % 3 == 0:
            for number in range(len(element)):
                
