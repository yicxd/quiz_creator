question = input("Enter a question: ")
sep_question = question + "\n" #seperates the questions by lines, for organizing
question_file = open("questions.txt", "a")#opens file name and a is append
question_file.write(sep_question)
question_file.close()

for i in range(4):
    answers = input(f"Enter four answers for that question No {i+1}:")
    sep_answers = answers + "\n"
    answer_file = open("answers.txt", "a")
    answer_file.write(sep_answers)
    answer_file.close()