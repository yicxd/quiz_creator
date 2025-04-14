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

        window = QWidget() #this is the receiver of mouse and keyboard actions
        window.setWindowTitle("Quiz Creator") #title
        window.setFixedSize(500, 600) #resolution of the window
        
        #layout type and spacing
        layout = QFormLayout()
        layout.setVerticalSpacing(15)
        layout.setHorizontalSpacing(20) 
        layout.setContentsMargins(30, 30, 30, 30)

        question = 0
        answers = 0

        sep_question = str(question) + "\n" #seperates the questions by lines, for organizing
        question_file = open("questions.txt", "a") #opens file name and a is append
        question_file.write(sep_question) #will write the input in the txt file
        question_file.close()

        sep_answers = str(answers) + "\n"
        answer_file = open("answers.txt", "a")
        answer_file.write(sep_answers)
        answer_file.close()

        layout.addRow(QLabel("Question:")) #adds a row to accept input
        layout.addRow(QLabel("a):"))
        layout.addRow(QLabel("b):"))
        layout.addRow(QLabel("c):"))
        layout.addRow(QLabel("d):"))
        layout.addRow(QLabel("What is the correct answer?:"))

if __name__ == "__main__":
    app = QApplication([]) #this is the application that will open
    
    font = QFont()
    font.setFamily("Arial")
    app.setFont(font)
    
    window = quiz()
    window.show()
    sys.exit(app.exec())