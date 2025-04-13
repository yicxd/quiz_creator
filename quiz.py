import sys
from PyQt6.QtWidgets import ( 
    QApplication, QFormLayout, QLineEdit, QWidget, 
    QLabel, QComboBox, QCheckBox, QPushButton
)

app = QApplication([]) #this is the application that will open
window = QWidget() #this is the receiver of mouse and keyboard actions
window.setWindowTitle("Quiz Creator") #title
window.setFixedSize(500, 600) #resolution of the window
layout = QFormLayout() #Qformlayout uses a form layout

#spacing of the layout
layout.setVerticalSpacing(15)
layout.setHorizontalSpacing(20) 
layout.setContentsMargins(30, 30, 30, 30)


while True:
    window.setLayout(layout)
    window.show() #will open the window
    try:
        layout.addRow(QLabel("Question:"))
        sep_question = question + "\n" #seperates the questions by lines, for organizing
        question_file = open("questions.txt", "a") #opens file name and a is append
        question_file.write(sep_question) #will write the input in the txt file
        question_file.close()

        for i in range(97, 101):
            layout.addRow("Option " + chr(i) + ") ", QLineEdit())
            answers = input("Enter four answers for that question - Option " + chr(i) + ") ")#used characters as choices
            sep_answers = answers + "\n"
            answer_file = open("answers.txt", "a")
            answer_file.write(sep_answers)
            answer_file.close()

        correct = None
        while correct not in {"a", "b", "c", "d", "A", "B", "C", "D"}:
            correct = input('Which one is the correct answer? a, b, c, d: ')
            continue

        again = input("If you would like to test this code again type '1' and if you want to end it all type anything: ")
        if again == "1":
            continue
        else:
            exit()
            sys.exit(app.exec()) #the application will also close

    except ValueError:
        print("how did you trigger ValueError?")
