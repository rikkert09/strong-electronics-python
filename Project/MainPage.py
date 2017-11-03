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

        ''''
        ALL LABELS FOR MAINPAGE
        '''
        # a line of text
        label1 = tk.Label(self, text="Besturingseenheid")
        label1.grid(row=1, column=0)

        # a row of white space
        label2 = tk.Label(self)
        label2.grid(row=2, column=0, sticky="E")

        # a line of text
        label2 = tk.Label(self, text="Uitgerold:")
        label2.grid(row=3, column=0)

        # a line of text
        label3 = tk.Label(self, text="Sensorwaarde:")
        label3.grid(row=4, column=0)

        ''''
        ALL BUTTONS FOR MAINPAGE
        '''
        # Button to roll up the sunshade
        but1 = ttk.Button(self, text="Oprollen", width=10)
        but1.grid(row=5, column=0)

        # Button to roll out the sunshade
        but2 = ttk.Button(self, text="Uitrollen", width=10)
        but2.grid(row=6, column=0)

        # Button to go to detailed information about a particulair Controlunit
        but3 = ttk.Button(self, text="Overzicht", width=10,
                          command=lambda: controller.show_frame("ControlUnit"))
        but3.grid(row=7, column=0)