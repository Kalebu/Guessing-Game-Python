from random import randint
from tkinter import Label, Button, Tk, Entry

class GuessingGame:
    def __init__(self, window):
        window.title('Guessing Game');window.geometry('400x150');window.resizable(0,0)
        self.magic_number = self.new_random
        self.question = Label(window, font=('Times', 11))
        self.guess_result = Label(window, font=('Times', 11))
        self.entry_answer = Entry()
        self.guess_button = Button(window,text='Guess number', bg='red', command=self.check_guess)
        self.question.place(x=20, y=10);self.entry_answer.place(x=120, y=50)
        self.guess_button.place(x=140, y=80);self.guess_result.place(x=100, y=120)
        self.new_random()

    def new_random(self):
        magic = lambda : randint(1, 500)
        guess_range = sorted([magic(), magic()])
        guess_text = 'I\'ve number btn {} and {} can you guess it ?'.format(guess_range[0], guess_range[1])
        self.question.configure(text = guess_text)
        self.magic_number = randint(guess_range[0], guess_range[1])

    def check_guess(self):
        try:
            number = int(self.entry_answer.get())
            if self.magic_number>number:
                self.guess_result.configure(text = 'Your number is low ')
            elif self.magic_number<number:
                self.guess_result.configure(text='Your number is high')
            else:
                self.guess_result.configure(text='Congratulation you made it')
                self.new_random()
        except:
            pass

window = Tk()
app = GuessingGame(window)
window.mainloop()