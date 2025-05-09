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
        self.score = 0
        self.question_count = 0
        self.used_question_num = set()#tracks which questions have been used
        self.total_questions = 0

        #calling the functions
        self.widgets()
        self.preload_questions()
        self.questions()

    def preload_questions(self): #preloading the questions instead of loading one by one
        #file management
        with open("questions.txt") as question:
            self.all_questions = [quest.strip() for quest in question.readlines()]

        with open("answers.txt") as answer:
            self.all_answers = [line.strip() for line in answer.readlines()]
        
        self.total_questions = len(self.all_questions)

    def check_answer(self):
        #checks if an option is selected
        if not self.selected_option.get():
            messagebox.showwarning("No Selection", "Please select an answer.")
            return False
        
        #check if the answer is correct
        is_correct = (self.selected_option.get() == self.current_question["correct"])
        if is_correct:
            self.score += 1
        
        #updates score display
        self.score_label.config(text=f"Score: {self.score}")
        return True
            
    def questions(self):
        #only continues if there is a answer selected
        if self.question_count > 0 and not self.check_answer():
            return
        
        #checks if all questions have been used
        if len(self.used_question_num) >= self.total_questions:
            messagebox.showinfo("Quiz Complete", 
            f"Final score: {self.score}")
            self.next_button.config(state=tk.DISABLED)
            return
        
        #get a random question that hasnt shown yet
        available_num = set(range(self.total_questions)) - self.used_question_num
        random_num = random.choice(list(available_num))
        self.used_question_num.add(random_num)

        #print the quiz
        rand_quest = self.all_questions[random_num]
        choices = self.all_answers[random_num * 2]
        correct_ans = self.all_answers[(random_num * 2) + 1]

        correct_ans = correct_ans.split(": ")[1].strip()
        options = [opt.strip() for opt in choices.split(',')]

        #stores everything in a list
        self.quiz_data = [{
                "question": rand_quest,
                "options": options,
                "correct": correct_ans
        }]

        #label of question
        self.current_question = self.quiz_data[0]
        
        #updates the current display
        self.question_label.config(text=self.current_question["question"])

        #clears previous option
        for widget in self.options_frame.winfo_children():
            widget.destroy()

        #buttons for option
        for option in self.current_question["options"]:
            button = ttk.Radiobutton(self.options_frame, text=option, 
            variable=self.selected_option,value=option[0])
            button.pack(anchor=tk.W, pady=5, ipady=5)
        
        #resets the selections
        self.selected_option.set("")

        #+1 for every question asked
        self.question_count += 1
        self.score_label.config(text=f"Score: {self.score}")

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

        #a next question button
        self.button_frame = ttk.Frame(self.window)
        self.button_frame.pack(pady=20)
        
        self.next_button = ttk.Button(self.button_frame, 
        text="Next Question", command=self.questions)
        self.next_button.pack(side=tk.LEFT, padx=10)

        #score progress bar
        self.progress_frame = ttk.Frame(self.window)
        self.progress_frame.pack(pady=10)
        self.score_label = ttk.Label(self.progress_frame, text=f"Score: {self.score}")
        self.score_label.pack(side=tk.RIGHT, padx=10)

if __name__ == "__main__":
    root = tk.Tk()
    app = the_quiz(root)
    root.mainloop()