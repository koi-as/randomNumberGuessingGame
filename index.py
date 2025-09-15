import tkinter as tk
from tkinter import *
import random

# create a gui
win=tk.Tk()
win.geometry('750x750')
win.title('Gessit')

# randint() function to randomly generate a number
# between 1 and 100. Function comes from random
# library
num=random.randint(1,100)

# assigning variables to functions
hint=StringVar()
score=IntVar()
finalScore=IntVar()
guess=IntVar()

# setting variable values
hint.set('Guess a number between 1 to 100')
score.set(5)
finalScore.set(score.get())
# using set method we set what will be value of
# variables when they are displayed in window

def fun():
    x=guess.get()
    finalScore.set(score.get())
    if score.get()>0:
        if x>20 or x<0:
            hint.set('You lost a chance!')
            score.set(score.get()-1)
            finalScore.set(score.get())
        elif num==x:
            hint.set('Congrats, you won!')
            score.set(score.get()-1)
            finalScore.set(score.get())
        elif num>x:
            hint.set('You guessed too low, try again...')
            score.set(score.get()-1)
            finalScore.set(score.get())
        elif num<x:
            hint.set('You guessed too high, try again...')
            score.set(score.get()-1)
            finalScore.set(score.get())
    else:
        hint.set('HA, you lost! Better luck next time...')
# function fun compares user guess to randomly
# generated number. First comparison is if the
# guess is not in range. Second comparison is
# if guess is correct. Third and fourth compare
# if guess was too low or high respectively.

# By setting the value of hint, we change the
# text displayed in the game window. 

Entry(win, textvariable=guess, width=3, font=('Ubuntu', 50), relief=GROOVE).place(relx=0.5, rely=0.3, anchor=CENTER)
Entry(win, textvariable=hint, width=50, font=('Courier', 15), relief=GROOVE, bg='orange').place(relx=0.5, rely=0.7, anchor=CENTER)
Entry(win, text=finalScore, width=2, font=('Ubuntu', 24), relief=GROOVE).place(relx=0.5, rely=0.85, anchor=CENTER)
Label(win, text='Guess the number, foo', font=('Courier', 25)).place(relx=0.5, rely=0.09, anchor=CENTER)
Label(win, text='Score out of 5', font=('Courier', 25)).place(relx=0.3, rely=0.85, anchor=CENTER)
Button(win, width=8, text='GUESS', font=('Courier', 25), command=fun, relief=GROOVE, bg='light blue').place(relx=0.5, rely=0.5, anchor=CENTER)

# win calls the win variable equal to tk.Tk()
# what is tk.Tk()?

# textvariable versus text? Is textvariable 
# something that the user can change, versus 
# text which is just static

# font sets the font for the item. At least
# two arguments: font name and font size (in px?)

win.mainloop()