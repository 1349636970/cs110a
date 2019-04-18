import random
# def main():
#     correct_answer_file = open("Correct_answer",'r')
#     correct_answer = []
#     user_answer_file = open("user_answer",'r')
#     user_answer = []
#     wrong_answer_count = 0
#     for line in correct_answer_file:
#         correct_answer.append(line.rstrip('\n'))
#     correct_answer_file.close()
#     for line in user_answer_file:
#         user_answer.append(line.rstrip('\n'))
#     user_answer_file.close()
#     print(check_answer(correct_answer, wrong_answer_count, user_answer))


# # def check_answer(correct_answer, wrong_answer_count, user_answer):
#     for student_answer in range(20):
#         if user_answer[student_answer] != correct_answer[student_answer]:
#             wrong_answer_count += 1
#         if wrong_answer_count >= 5:
#             return "You fail!"
#     if wrong_answer_count < 5:
#         return "You pass"

# def main():
#     try:
#         file_open = open("USPopulation.txt",'r')
#     except IOError as e:
#         print(e)
#     USPopulation_list = []
#     for line in file_open:
#         USPopulation_list.append(int(line.rstrip('\n')))
#     file_open.close()
#     print("average:",sum(USPopulation_list)/(1990-1950))
#     print("Max", 1950+int(USPopulation_list.index(max(USPopulation_list))))
#     print("Min", 1950+int(USPopulation_list.index(min(USPopulation_list))))

# def large_file():
#     try:
#         file_open = open("USPopulation.txt", 'r')
#     except IOError as e:
#         print(e)
#     diff = 0
#     for line in file_open:
#         current_number = int(file_open.readline().rstrip('\n'))
#         if current_number > maximum:
#             diff = current_number

def main():
    try:
        file_open = open("8_ball_responses.txt", 'r')
    except IOError as e:
        print(e)
    file_list = file_open.readlines()
    file_open.close()
    while (input("Enter your question: ") != "!q"):
        print(file_list[random.randint(0,len(file_list))])
    
    

main()


