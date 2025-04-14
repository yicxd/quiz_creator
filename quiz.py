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

        #adds a row to accept input
        layout.addRow(QLabel("Question:"), self.question)
        layout.addRow(QLabel("a):"), self.a)
        layout.addRow(QLabel("b):"), self.b)
        layout.addRow(QLabel("c):"), self.c)
        layout.addRow(QLabel("d):"), self.d)
        layout.addRow(QLabel("Correct answer:"), self.correct)

        #a submit button
        submit = QPushButton("Submit")
        submit.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        submit.clicked.connect(self.save_data)
        layout.addRow(submit)

    def save_data(self): #saves the question and answers to files
        quest = self.question.text()
        a = self.a.text()
        b = self.b.text()
        c = self.c.text()
        d = self.d.text()
        correct = self.correct.currentText()

        #now formatted and organized
        quest_file = open("questions.txt", "a")
        quest_file.write(f"{quest}\n")

        answer_file = open("answers.txt", "a")
        answer_file.write(f"a) {a}, b) {b}, c) {c}, d) {d}\nCorrect: {correct}\n")

        print("Saved")


if __name__ == "__main__":
    app = QApplication(sys.argv) #this is the application that will open
    
    font = QFont()
    font.setFamily("Arial")
    app.setFont(font)
    
    window = quiz()
    window.show()
    sys.exit(app.exec())