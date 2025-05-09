import sys
import tkinter as tk
from tkinter import ttk, messagebox
import random

class the_quiz():
    def __init__(self, root):
        self.window = root
        self.window.title("Quiz")
        
        #centerinng the window
        screen_width = self.window.winfo_screenwidth() #your resolution
        screen_height = self.window.winfo_screenheight()
        center_x = int(screen_width/2 - 800/2)
        center_y = int(screen_height/2 - 600/2)
        self.window.geometry(f'{800}x{600}+{center_x}+{center_y}')

        #quiz variables
        self.selected_option = tk.StringVar()
        self.current_question = None

        #calling the functions
        self.widgets()
        self.questions()

            
    def questions(self):
        #file management
        question = open("questions.txt")
        quest_line = question.readlines()
        total_lines = len(quest_line)
        question.close()

        answer = open("answers.txt")
        ans_line = answer.readlines()
        question.close()

        #randomization
        random_num = random.randrange(0, total_lines)

        #print the quiz
        rand_quest = quest_line[random_num]
        choices = ans_line[random_num * 2]
        correct_ans = ans_line[(random_num * 2) + 1]

        #stores everything in a list
        self.quiz_data = []
        self.quiz_data.append({
                    "question": rand_quest,
                    "options": choices,
                    "correct": correct_ans
                })

        #label of question
        self.current_question = self.quiz_data
        
        #updates the current display
        self.question_label.config(text=self.current_question["question"])

        #buttons for option
        for option in ["options"]:
            button = ttk.Radiobutton(self.options_frame, text=option.strip(), 
            variable=self.selected_option,value=option.strip())
            button.pack(anchor=tk.W, pady=5, ipady=5)
        
        #resets the selections
        self.selected_option.set("")

    def widgets(self):
        #frame for questions
        self.question_frame = ttk.Frame(self.window)
        self.question_frame.pack(pady=20, padx=20, fill=tk.BOTH, expand=True)
        
        self.question_label = ttk.Label(self.question_frame, 
        text="", font=('Arial', 15, 'bold'), wraplength=700, 
        justify=tk.CENTER)
        self.question_label.pack(pady=10)

        #frame for answers
        self.options_frame = ttk.Frame(self.question_frame)
        self.options_frame.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = the_quiz(root)
    root.mainloop()