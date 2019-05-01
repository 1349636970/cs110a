# File: Ch15-Wed.py
# Description: Write a program that asks the user to enter five test scores. The program should display a letter grade for each score and the average test score. Write the following functions in the program: calc_average. This function should accept five test scores as arguments and return the average of the scores. determine_grade.

def calc_average(test_score1,test_score2,test_score3,test_score4,test_score5):
    test_score_list = [test_score1,test_score2,test_score3,test_score4,test_score5]
    return sum(test_score_list)/len(test_score_list)

def determine_grade(test_score):
    result = None
    if test_score > 100 or test_score < 0:
        result = "Invalid test score"
    if test_score >= 90:
        result = 'A'
    elif test_score >= 80:
        result = 'B'
    elif test_score >= 70:
        result = 'C'
    elif test_score >= 60:
        result = 'D'
    else:
        result = 'F'
    return result

def main():
    score_list = []
    for x in range(5):
        score = int(input("Your score: "))
        grade = determine_grade(score)
        print(grade)
        score_list.append(score)
    print("averge grade: ",calc_average(*score_list))

main()


# Your score: 8
# F
# Your score: 80
# B
# Your score: 90
# A
# Your score: 6
# F
# Your score: 75
# C
# averge grade:  51.8