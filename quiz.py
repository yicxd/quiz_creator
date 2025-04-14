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
        question = layout.addRow(QLabel("Question:")) #adds a row to accept input
        sep_question = str(question) + "\n" #seperates the questions by lines, for organizing
        question_file = open("questions.txt", "a") #opens file name and a is append
        question_file.write(sep_question) #will write the input in the txt file
        question_file.close()

        for i in range(97, 101): #97 is 'a' in character
            answers = layout.addRow(QLabel("Enter four answers for that question - Option " + chr(i) + ") "))#switches the number into characters
            sep_answers = str(answers) + "\n"
            answer_file = open("answers.txt", "a")
            answer_file.write(sep_answers)
            answer_file.close()

        correct = None
        while correct not in {"a", "b", "c", "d", "A", "B", "C", "D"}:
            correct = layout.addRow(QLabel("Which one is the correct answer? a, b, c, d: "))
            continue
        else:
            break

#will use a button instead for retries

    except ValueError:
        print("how did you trigger ValueError?")

sys.exit(app.exec())
