question = input("Enter a question: ")

file = open("questions.txt", "a")#opens file name and a is append
file.write(question)