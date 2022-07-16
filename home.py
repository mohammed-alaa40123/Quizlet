from tkinter import *
import random
THEME_COLOR = "#375362"


class Home:
    def __init__(self):
        self.category = 0
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.heading = Label(text="SELECT A TOPIC FOR QUIZ", padx=10, pady=10,
                             font=("Arial", 20, "bold"), bg=THEME_COLOR)
        self.heading.grid(column=0, row=0, columnspan=2)

        self.comp_quiz = Button(text="Computers", width=20, command=self.computers, padx=10, pady=10)
        self.comp_quiz.grid(column=0, row=1)
        self.gk_quiz = Button(text="General Knowledge", width=20, command=self.gk, padx=10, pady=10)
        self.gk_quiz.grid(column=1, row=1)
        self.ent_quiz = Button(text="Entertainment", width=20, command=self.entertainment, padx=10, pady=10)
        self.ent_quiz.grid(column=0, row=3)
        self.sports_quiz = Button(text="Sports", width=20, command=self.sports, padx=10, pady=10)
        self.sports_quiz.grid(column=1, row=3)
        self.geo_quiz = Button(text="Geography", width=20, command=self.geography, padx=10, pady=10)
        self.geo_quiz.grid(column=0, row=5)
        self.hist_quiz = Button(text="History", width=20, command=self.history, padx=10, pady=10)
        self.hist_quiz.grid(column=1, row=5)

        self.window.mainloop()

    def entertainment(self):
        self.category = random.choice([11, 12, 14, 15])
        self.window.destroy()

    def sports(self):
        self.category = 21
        self.window.destroy()

    def history(self):
        self.category = 23
        self.window.destroy()

    def geography(self):
        self.category = 22
        self.window.destroy()

    def gk(self):
        self.category = 9
        self.window.destroy()

    def computers(self):
        self.category = 18
        self.window.destroy()
