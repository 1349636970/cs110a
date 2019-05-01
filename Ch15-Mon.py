# File: Ch15.py
# Description: Write a program that uses nested loops to draw this pattern:

##
# #
#  #
#   #
#    #
#     #


def main():
    count = 0
    for x in range(6):
        print('#',end='')
        for y in range(count):
            print(' ',end='')
        print('#')
        count += 1
main()
        

# ~/coding/cs110a   master  /usr/bin/python3 /home/yingzheng/coding/cs110a/Ch15-Mon.py
# ##
# # #
# #  #
# #   #
# #    #
# #     #
#  ~/coding/cs110a   master  

def bonus():
    symbol = input('Enter symbol: ')
    height = int(input('Enter height: '))
    count = height
    space_count = 0
    for x in range(1,2*height+1):
        if x >= height+1:
            space_count += 1
            for space in range(space_count):
                print(" ",end='')
            for z in range(count-1):
                print(symbol,end='')
            count -= 1
        else:
            for y in range(x):
                print(symbol,end='')
        
        print()

bonus()
# Enter symbol: &
# Enter height: 7
# &
# &&
# &&&
# &&&&
# &&&&&
# &&&&&&
# &&&&&&&
#  &&&&&&
#   &&&&&
#    &&&&
#     &&&
#      &&
#       &