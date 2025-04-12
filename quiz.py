question = input("Enter a question: ")

for i in range(4):
    answers = input(f"Enter four answers for that question No {i+1}:")

question_file = open("questions.txt", "a")#opens file name and a is append
question_file.write(question)
question_file.close()

answer_file = open("answers.txt", "a")
answer_file.write(answers)
answer_file.close()