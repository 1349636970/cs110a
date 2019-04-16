def main():
    correct_answer_file = open("Correct_answer",'r')
    correct_answer = []
    user_answer_file = open("user_answer",'r')
    user_answer = []
    wrong_answer_count = 0
    for line in correct_answer_file:
        correct_answer.append(line.rstrip('\n'))
    correct_answer_file.close()
    for line in user_answer_file:
        user_answer.append(line.rstrip('\n'))
    user_answer_file.close()
    print(check_answer(correct_answer, wrong_answer_count, user_answer))


def check_answer(correct_answer, wrong_answer_count, user_answer):
    for student_answer in range(20):
        if user_answer[student_answer] != correct_answer[student_answer]:
            wrong_answer_count += 1
        if wrong_answer_count >= 5:
            return "You fail!"
    if wrong_answer_count < 5:
        return "You pass"
main()
