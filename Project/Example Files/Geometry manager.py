from tkinter import *
from tkinter import ttk

root = Tk()

label_1 = Label(root, text='Username')
label_2 = Label(root, text='Password')
entry_1 = Entry(root)
entry_2 = Entry(root)
c = Checkbutton(root, text="Keep me logged in")


label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
c.grid(columnspan=2)

root.mainloop()