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
        Mainpage.newc(self, 0)
        Mainpage.newc(self, 1)
        Mainpage.newc(self, 2)
        Mainpage.newc(self, 3)
        # Mainpage.newc(self, 4)

        ''''
        ALL LABELS FOR MAINPAGE
        '''

    def newc(self, col):
        marginframe = ttk.Frame(self, padding=10)  # generates a frame within the frame with padding set to 10
        marginframe.grid(row=1, column=col)
        borderframe = ttk.LabelFrame(marginframe, padding=10)  # generates a labelframe within frame. padding set to 10
        borderframe.grid(row=1)

        # print(borderframe.grid_info())

        # a line of text
        label1 = tk.Label(borderframe, text="Besturingseenheid")
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