import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

''''
The class Mainpage is the front page of the application
It's a frame that shows which controlunit(s) are connected
'''

class Mainpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        names = ["Besturingseenheid 1", "Besturingseenheid 2", "asdasd 3"]
        for i in names:
            Mainpage.newc(self, i, names.index(i)) # passes the string and index position in the list of names

        # Mainpage.newc(self, name, 0)
        # Mainpage.newc(self, name, 1)
        # Mainpage.newc(self, 2)
        # Mainpage.newc(self, 3)
        # Mainpage.newc(self, 4)

        ''''
        ALL LABELS FOR MAINPAGE
        '''

    def newc(self, name, col): # name is a string and col is the index position at which to place the control unit
        marginframe = tk.Frame(self, padx=10, pady=10, width=300)  # generates a frame within the frame with padding set to 10
        marginframe.grid(row=1, column=col)
        borderframe = tk.Frame(marginframe, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
        # generates a tk.frame within another frame, to get the padding/margin right. padx/pady set to 10
        borderframe.grid(row=1)

        # print(borderframe.grid_info())

        # a line of text
        label1 = tk.Label(borderframe, text=name)
        label1.grid(row=1, column=0)

        # a row of white space
        label2 = tk.Label(borderframe)
        label2.grid(row=2, column=0)

        # a line of text
        label2 = tk.Label(borderframe, text="Uitgerold:")
        label2.grid(row=3, column=0)

        # a line of text
        label3 = tk.Label(borderframe, text="Sensorwaarde:")
        label3.grid(row=4, column=0)

        ''''
        ALL BUTTONS FOR MAINPAGE
        '''
        # Button to roll up the sunshade
        but1 = ttk.Button(borderframe, text="Oprollen", width=10)
        but1.grid(row=5, column=0)

        # Button to roll out the sunshade
        but2 = ttk.Button(borderframe, text="Uitrollen", width=10)
        but2.grid(row=6, column=0)

        # Button to go to detailed information about a particulair Controlunit
        but3 = ttk.Button(borderframe, text="Overzicht", width=10,
                          command=lambda: self.controller.show_frame("ControlUnit"))
        but3.grid(row=7, column=0)