import sys
from PyQt6.QtWidgets import ( 
    QApplication, QFormLayout, QLineEdit, QWidget, 
    QLabel, QComboBox, QCheckBox, QPushButton
)

class quiz(QWidget):
    def __init__(self):
        super().__init__()

        app = QApplication([]) #this is the application that will open
        window = QWidget() #this is the receiver of mouse and keyboard actions
        window.setWindowTitle("Quiz Creator") #title
        window.setFixedSize(500, 600) #resolution of the window
        
        #layout type and spacing
        layout = QFormLayout()
        layout.setVerticalSpacing(15)
        layout.setHorizontalSpacing(20) 
        layout.setContentsMargins(30, 30, 30, 30)


        app.exec()
        window.setLayout(layout)
        window.show() #will open the window

        question = layout.addRow(QLabel("Question:")) #adds a row to accept input
        sep_question = str(question) + "\n" #seperates the questions by lines, for organizing
        question_file = open("questions.txt", "a") #opens file name and a is append
        question_file.write(sep_question) #will write the input in the txt file
        question_file.close()

        answers = layout.addRow(QLabel("Enter four answers for that question - Option " + chr(i) + ") "))#switches the number into characters
        sep_answers = str(answers) + "\n"
        answer_file = open("answers.txt", "a")
        answer_file.write(sep_answers)
        answer_file.close()