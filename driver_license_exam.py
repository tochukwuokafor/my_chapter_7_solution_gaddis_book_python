def main():
    correct_answers = ['A', 'C', 'A', 'A', 'D', 'B', 'C', 'A', 'C', 'B', 'A', 'D', 'C', 'A', 'D', 'C', 'B', 'B', 'D', 'A']
    open_file = open('driver_license_exam.txt', 'r')
    student_answers = []
    for answer in open_file:
        answer = answer[:-1]
        student_answers.append(answer)
    open_file.close()
    #print(student_answers)
    grading = []
    for i in range(20):
        if student_answers[i] == correct_answers[i]:
            grading.append(True)
        else:
            grading.append(False)
    if grading.count(True) >= 15:
        print('The student passed the exam.')
    else:
        print('The student failed the exam.')
    print('The total number of correctly answered questions is', grading.count(True))
    print('The total number of incorrectly answered questions is', grading.count(False))
    incorrect_question = []
    for index, value in enumerate(grading):
        if value == False:
            index = index + 1
            incorrect_question.append(index)
    print(incorrect_question)

main()