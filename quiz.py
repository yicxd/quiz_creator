import sys
from PyQt6.QtWidgets import ( 
    QApplication, QFormLayout, QLineEdit, QWidget, #these are the main functions for the gui
    QLabel, QComboBox, QPushButton, QTextEdit
)
from PyQt6.QtGui import QFont, QPalette, QColor #these are for aesthetics
from PyQt6.QtCore import Qt #for alignment

class quiz(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Quiz Creator") #title of the window
        self.setFixedSize(500, 600) #resolution of the window
        
        #color palette of the gui
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(200, 240, 255)) #light cyan background
        palette.setColor(QPalette.ColorRole.WindowText, QColor(0, 70, 90)) #dark teal text
        palette.setColor(QPalette.ColorRole.Base, QColor(220, 255, 255)) #very light cyan for input bar background
        palette.setColor(QPalette.ColorRole.Text, QColor(0, 100, 120)) #teal text for inputs
        palette.setColor(QPalette.ColorRole.PlaceholderText, QColor(0, 0, 0)) #black for placeholder text
        self.setPalette(palette)
        
        #layout type and spacing
        layout = QFormLayout()
        layout.setVerticalSpacing(15)
        layout.setHorizontalSpacing(20) 
        layout.setContentsMargins(30, 30, 30, 30)
        self.setLayout(layout)

        #title inside the gui
        title = QLabel("Quiz Creator")
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)
        title.setFont(title_font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addRow(title)

        layout.addRow(QLabel(" ")) #for spacing only

        #assigns what type of row for input
        self.question = QTextEdit(placeholderText="Enter here")
        self.a = QLineEdit(placeholderText="Enter here")
        self.b = QLineEdit(placeholderText="Enter here")
        self.c = QLineEdit(placeholderText="Enter here")
        self.d = QLineEdit(placeholderText="Enter here")
        self.correct = QComboBox()
        self.correct.addItems(["a", "b", "c", "d"])

        #adds the row to accept input
        layout.addRow(QLabel("Question:"), self.question)
        layout.addRow(QLabel("a):"), self.a)
        layout.addRow(QLabel("b):"), self.b)
        layout.addRow(QLabel("c):"), self.c)
        layout.addRow(QLabel("d):"), self.d)
        layout.addRow(QLabel("Correct answer:"), self.correct)

        #a submit button
        submit = QPushButton("Save")
        submit.setFont(QFont("Arial", 10, QFont.Weight.Bold))
        submit.setStyleSheet("""
            QPushButton{
                background-color: #39c5bb;
                color: white;
                border-radius: 10px;
                padding: 8px;
            }
            QPushButton:hover{
                background-color: #2da89e;
            }      
        """) #literally css
        submit.clicked.connect(self.save_data)
        layout.addRow(submit)

    def save_data(self): #saves the question and answers to files
        quest = self.question.toPlainText()
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