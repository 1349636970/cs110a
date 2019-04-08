# File: Ch12-Mon.py
# Description: A Personal Fitness Tracker is a wearable device that tracks your physical activity, calories burned, heart rate, sleeping patterns, and so on. One common physical activity that most of these devices track is the number of steps you take each day.

# If you have downloaded this book’s source code from the Computer Science Portal, you will find a file named steps.txt in the Chapter 06 folder.Preview the document  The steps.txt file contains the number of steps a person has taken each day for a year. There are 365 lines in the file, and each line contains the number of steps taken during a day. (The first line is the number of steps taken on January 1st, the second line is the number of steps taken on January 2nd, and so forth.) Write a program that reads the file, then displays the average number of steps taken for each month. (The data is from a year that was not a leap year, so February has 28 days.)

def main():
    sum = 0
    try:
        filename = open("steps.txt",'r')
    except IOError as e:
        print(e)
    for line in filename:
        sum += int(line.strip("\n"))
    filename.close()
    print("average is:", format(sum/365,'.2f'))
main()
    
