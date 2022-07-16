import subprocess
from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(height=400, width=400, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2)
        self.tru_img = PhotoImage(file="images/true.png")
        self.fls_img = PhotoImage(file="images/false.png")
        self.true_Button = Button(image=self.tru_img, highlightthickness=0, padx=40, pady=40,
                                  command=self.user_pressed_true)
        self.False_button = Button(image=self.fls_img, highlightthickness=0, padx=40, pady=40,
                                   command=self.user_pressed_false)
        self.card = Canvas(height=100, width=300, bg=THEME_COLOR, highlightthickness=0)
        self.card.grid(column=0, row=2, columnspan=2)
        self.true_Button.grid(column=0, row=3)
        self.False_button.grid(column=1, row=3)
        self.score = self.card.create_text(270, 50, text=f"Score:0", font=("Arial", 10, "bold"), fill="black")
        try:
            with open("score.txt", mode="r") as data:
                self.highest_score = int(data.read())
        except FileNotFoundError:
            self.high_score = self.card.create_text(50, 50, text=f"Highest Score:0", font=("Arial", 10, "bold"),
                                                    fill="black")
            self.highest_score = 0
        else:
            self.high_score = self.card.create_text(50, 50, text=f"Highest Score:{self.highest_score}", font=("Arial", 10, "bold"), fill="black")
        self.question = self.canvas.create_text(150, 150, width=300, text=f"Question goes here",
                                                font=("Arial", 20, "bold"),
                                                fill=THEME_COLOR)
        self.card_background = self.canvas.config(height=300, width=300, bg="white")
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question, text=q_text)

    def user_pressed_true(self):
        user_answer = 'true'
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def user_pressed_false(self):
        user_answer = 'false'
        is_right = self.quiz.check_answer(user_answer)
        self.give_feedback(is_right)

    def give_feedback(self, is_right, ):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        if self.quiz.still_has_questions():
            self.card.itemconfig(self.score, text=f"score:{self.quiz.score}", font=("Arial", 10, "bold"), fill="black")
        else:
            self.canvas.itemconfig(self.question, text=f" Game Over\n\nYour score:{self.quiz.score}", font=("Arial", 30, "bold"), fill="black")
            self.true_Button.config(state="disabled")
            self.False_button.config(state="disabled")
            self.window.after(2000, self.restart)
            print(self.quiz.score)
            if self.quiz.score > self.highest_score:
                with open("score.txt", mode="w") as data:
                    data.write(f"{self.quiz.score}")

    def restart(self):
        self.true_Button.destroy()
        self.False_button.destroy()
        restart_btn = Button(text="RESTART", padx=10, pady=10, highlightthickness=0, command=self.start_new_quiz)
        restart_btn.grid(column=0, row=2)
        exit_btn = Button(text="EXIT", padx=10, pady=10,  highlightthickness=0, command=self.window.destroy)
        exit_btn.grid(column=1, row=2)

    def start_new_quiz(self):
        self.window.destroy()
        subprocess.call(['python', 'main.py'])
