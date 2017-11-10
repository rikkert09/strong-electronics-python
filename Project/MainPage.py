import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk
#import serial.tools.list_ports

''''
The class Mainpage is the front page of the application
It's a frame that shows which controlunit(s) are connected
'''

class Mainpage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        names = ["Besturingseenheid 1", "Besturingseenheid 2", "Besturingseenheid 3"]
        for i in names:
            Mainpage.newc(self, i, names.index(i)) # passes the string and index position in the list of names



        ''''
        ALL LABELS FOR MAINPAGE
        '''
        # def scan(self):
        #     ports = list(serial.tools.list_ports.comports())
        #     for p in ports:
        #         print(p)
        #
        # scanbutton = ttk.Button(self, text="Scan for devices")
        # scanbutton.bind("<Button-1>", scan)
        # scanbutton.grid(row=0)

    def newc(self, name, col):  # name is a string and col is the index position at which to place the control unit
        marginframe = tk.Frame(self, padx=10, pady=10,
                               width=300)  # generates a frame within the frame with padding set to 10
        marginframe.grid(row=1, column=col)
        borderframe = tk.Frame(marginframe, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
        # generates a tk.frame within another frame, to get the padding/margin right. padx/pady set to 10
        borderframe.grid(row=1)

        # print(borderframe.grid_info())

        # a line of text
        namelabel = tk.Label(borderframe, text=name, width=20, height=7)
        namelabel.grid(row=0, column=0)

        # shows rollout status
        rolloutlabel = tk.Label(borderframe, text="Uiterold: ")
        rolloutlabel.grid(row=1, column=0, sticky=tk.N)

        # a row of white space
        rollout_value = tk.Label(borderframe, text=" 10 cm ")
        rollout_value.grid(row=2, column=0, sticky=tk.N)

        # shows sensor value
        sensorvaluelabel = tk.Label(borderframe, text="Sensorwaarde: ")
        sensorvaluelabel.grid(row=3, column=0, sticky=tk.N)

        # a row of white space
        sensorvalue = tk.Label(borderframe, text=" 10 ")
        sensorvalue.grid(row=4, column=0, sticky=tk.N)

        # a row of white space
        emptylabel = tk.Label(borderframe)
        emptylabel.grid(row=5, column=0)

        ''''
        ALL BUTTONS FOR MAINPAGE
        '''
        # Button to roll up the sunshade
        rollupbut = ttk.Button(borderframe, text="Oprollen", width=20)
        rollupbut.grid(row=6, column=0)

        # Button to roll out the sunshade
        rolloutbut = ttk.Button(borderframe, text="Uitrollen", width=20)
        rolloutbut.grid(row=7, column=0)

        # Button to go to detailed information about a particulair Controlunit
        overviewbut = ttk.Button(borderframe, text="Overzicht", width=20,
                                 command=lambda: self.controller.show_frame("ControlUnit"))
        overviewbut.grid(row=8, column=0)