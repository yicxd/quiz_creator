import sys
import tkinter as tk
from tkinter import ttk, messagebox
import random

class the_quiz():
    def __init__(self, root):
        self.window = root
        self.window.title("Quiz")

        #designs
        self.bg_color = "#fff5f5"
        self.highlight = "#ff9eb7"
        self.text_color = "#5a3d5a"
        self.accent = "#a8d8ea"
        
        self.window.configure(bg=self.bg_color)
        
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
            variable=self.selected_option,value=option[0], style='Bird.TRadiobutton')
            button.pack(anchor=tk.W, pady=5, ipady=5)
        
        #resets the selections
        self.selected_option.set("")

        #+1 for every question asked
        self.question_count += 1
        self.score_label.config(text=f"Score: {self.score}")

    def widgets(self):
        #style
        style = ttk.Style()
        style.configure('TFrame', background=self.bg_color)
        style.configure('TLabel', background=self.bg_color, foreground=self.text_color)
        style.configure('Bird.TRadiobutton', background=self.bg_color,
            foreground=self.text_color, font=('Arial', 11))
        style.configure('Black.TButton', background='black', foreground='black', 
                        font=('Arial', 11, 'bold'), borderwidth=0)
        
        header_frame = ttk.Frame(self.window)
        header_frame.pack(pady=10)
        
        self.header_label = ttk.Label(
            header_frame,
            text="✧･ﾟ: *✧･ﾟ:* Quiz *:･ﾟ✧*:･ﾟ✧",
            font=('Comic Sans MS', 16, 'bold'),
            foreground=self.highlight
        )
        self.header_label.pack()
        
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
        
        self.next_button = ttk.Button(self.button_frame, text="Next Question", 
            command=self.questions, style='Black.TButton')
        self.next_button.pack(side=tk.LEFT, padx=10)

        #score progress bar
        self.progress_frame = ttk.Frame(self.window)
        self.progress_frame.pack(pady=10)
        self.score_label = ttk.Label(self.progress_frame, text=f"Score: {self.score}")
        self.score_label.pack(side=tk.RIGHT, padx=10)

def start_quiz():
    welcome_window.destroy()
    quiz_window = tk.Tk()
    the_quiz(quiz_window)
    quiz_window.mainloop()

#a welcome page
welcome_window = tk.Tk()
welcome_window.title("Welcome to Hell!")
welcome_window.geometry("500x400")
welcome_window.configure(bg="#fff0f5")

screen_width = welcome_window.winfo_screenwidth()
screen_height = welcome_window.winfo_screenheight()
welcome_window.geometry(f"500x400+{(screen_width-500)//2}+{(screen_height-400)//2}")

header = tk.Label(welcome_window, text="(◕‿◕) Quiz Program (◕‿◕)", 
    font=("Comic Sans MS", 18, "bold"), bg="#fff0f5", fg="#8b008b")
header.pack(pady=30)

cat_art = tk.Label(welcome_window, text="""
∧＿∧
(｡･ω･｡)つ━☆・*。
⊂　　 ノ 　　　・゜+.
 しーＪ　　　°。+ *´¨)
　　　　　　.· ´¸.·*´¨) ¸.·*¨)
　　　　　　　　(¸.·´ (¸.·'* ☆
                """,
                font=("Courier New", 10),
                bg="#fff0f5",
                fg="#ff69b4")
cat_art.pack()

start_btn = tk.Button(welcome_window,
    text="START!", font=("Comic Sans MS", 14, "bold"),
    bg="#ff69b4", fg="white", bd=0, padx=20,
    pady=10, command=start_quiz)
start_btn.pack(pady=30)

welcome_window.mainloop()