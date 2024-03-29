from tkinter import *
import string
from tkinter import ttk


root = Tk()

class besturingseenheid:


    def __init__(self, master, col):
        f = Frame(master, highlightbackground="grey", highlightthickness=1, bd=0)
        row = 0
        nmbrofcols = 5
        if col >= nmbrofcols:
            row = int(col / nmbrofcols)
            col = col-nmbrofcols*row
        Label(f, text="Besturingseenheid").grid(row=0, column=0, sticky=W)

        label1 = Label(f, text="Temperatuur:")
        label1.grid(row=1, column=0, sticky=W)

        label2 = Label(f, text="Lichtintensiteit:")
        label2.grid(row=3, column=0, sticky=W)

        scale1 = Scale(f, from_=0, to=100, length=200, tickinterval=20, orient=HORIZONTAL)
        scale1.set(30)
        scale1.grid(row=2, column=0)

        scale2 = Scale(f, from_=0, to=100, length=200, tickinterval=20, orient=HORIZONTAL)
        scale2.set(70)
        scale2.grid(row=4, column=0)

        but1 = Button(f, text="Inrollen", width=10)
        but1.grid(row=5, column=0, sticky=S)

        but2 = Button(f, text="Uitrollen", width=10)
        but2.grid(row=6, column=0, sticky=S)

        but3 = Button(f, text="Overzicht", width=10)
        but3.grid(row=7, column=0, sticky=S)

        but4 = Button(f, text="edit")
        but4.grid(row=0, column=0, sticky=NE)

        f.grid(row=row, column=col, padx=25, pady=25)
        f.config(borderwidth=5)


for i in range(5):

    besturingseenheid(root, i)


root.title("Zeng Ltd Controller")
root.iconbitmap('Z.ico')
root.mainloop()
