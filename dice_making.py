from tkinter import *
from random import randint
def roll():
    text.delete(0.0, END)
    text.insert(END, str(randint(0,9)))
window = Tk ()
text =Text(window, width=35, height=35)
buttonA = Button(window, text='주사위를 굴리려면 누르세요!',command=roll)
text.pack()
buttonA.pack()
window.wait_window()