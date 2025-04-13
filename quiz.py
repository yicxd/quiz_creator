import sys
from PyQt6.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget

app = QApplication([]) #this is the application that will open
window = QWidget() #this is the receiver of mouse and keyboard actions
window.setWindowTitle("Quiz Creator") #title
window.setFixedSize(600, 400) #resolution of the window


while True:
    window.show() #will open the window
    try:
        question = input("Enter a question: ")
        sep_question = question + "\n" #seperates the questions by lines, for organizing
        question_file = open("questions.txt", "a") #opens file name and a is append
        question_file.write(sep_question) #will write the input in the txt file
        question_file.close()

        for i in range(4):
            answers = input(f"Enter four answers for that question No {i+1}: ")
            sep_answers = answers + "\n"
            answer_file = open("answers.txt", "a")
            answer_file.write(sep_answers)
            answer_file.close()

        again = input("If you would like to test this code again type '1' and if you want to end it all type anything: ")
        if again == "1":
            continue
        else:
            exit()
            sys.exit(app.exec()) #the application will also close

    except ValueError:
        print("how did you trigger ValueError?")
