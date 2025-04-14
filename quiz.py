import sys
from PyQt6.QtWidgets import ( 
    QApplication, QFormLayout, QLineEdit, QWidget, #these are the main functions for the gui
    QLabel, QComboBox, QCheckBox, QPushButton,
)
from PyQt6.QtGui import QFont #these are for aesthetics
from PyQt6.QtCore import Qt #for alignment

class quiz(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quiz Creator") #title
        self.setFixedSize(500, 600) #resolution of the window
        
        #layout type and spacing
        layout = QFormLayout()
        layout.setVerticalSpacing(15)
        layout.setHorizontalSpacing(20) 
        layout.setContentsMargins(30, 30, 30, 30)
        self.setLayout(layout)

        self.question = QLineEdit()
        self.question.setPlaceholderText("Enter here")

        self.a = QLineEdit()
        self.a.setPlaceholderText("Enter here")
        self.b = QLineEdit()
        self.b.setPlaceholderText("Enter here")
        self.c = QLineEdit()
        self.c.setPlaceholderText("Enter here")
        self.d = QLineEdit()
        self.d.setPlaceholderText("Enter here")

        self.correct = QComboBox()
        self.correct.addItems(["a", "b", "c", "d"])

        quest = layout.addRow(QLabel("Question:"), self.question) #adds a row to accept input
        a = layout.addRow(QLabel("a):"), self.a)
        b = layout.addRow(QLabel("b):"), self.b)
        c = layout.addRow(QLabel("c):"), self.c)
        d = layout.addRow(QLabel("d):"), self.d)
        correct = layout.addRow(QLabel("What is the correct answer?:"), self.correct)

        answers = a, b, c, d, correct
        sep_answers = str(answers) + "\n"
        answer_file = open("answers.txt", "a")
        answer_file.write(sep_answers)
        answer_file.close()

        sep_question = str(quest) + "\n" #seperates the questions by lines, for organizing
        question_file = open("questions.txt", "a") #opens file name and a is append
        question_file.write(sep_question) #will write the input in the txt file
        question_file.close()


if __name__ == "__main__":
    app = QApplication(sys.argv) #this is the application that will open
    
    font = QFont()
    font.setFamily("Arial")
    app.setFont(font)
    
    window = quiz()
    window.show()
    sys.exit(app.exec())