import tkinter as tk
from tkinter import font as tkfont
from tkinter import ttk

''''
The class ControlUnit is the page that will pop-up if you press the button "overzicht"
from the class Mainpage. The class ControlUnit is used as a overview to see data of a particulair
Controlunit in which you can adjust settings about that particulair Controlunit.
'''


class ControlUnit(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ''''
        ALL LABELS FOR CONTROLUNIT
        '''

        # Shows the name of the specific ControlUnit
        tk.Label(self, text="Besturingseenheid").grid(row=0, column=0, sticky=tk.W)

        # Text for the option to set the minimum roll out value of the sunshade
        label1 = tk.Label(self, text="Minimale Uitrol (in cm)")
        label1.grid(row=1, column=0, sticky=tk.W)

        # Text for the option to set the maximum roll out value of the sunshade
        label2 = tk.Label(self, text="Maximale Uitrol (in cm)")
        label2.grid(row=3, column=0, sticky=tk.W)

        # Text for the option to set the trigger value of the sensor
        label3 = tk.Label(self, text="Sensor Trigger")
        label3.grid(row=5, column=0, sticky=tk.W)

        # Text for the option to set the custom value of the sunshade
        label4 = tk.Label(self, text="Handmatig op/uitrollen (in cm)")
        label4.grid(row=7, column=0, sticky=tk.W)

        ''''
        ALL SCALES FOR CONTROLUNIT
        '''

        # Scale is the slidebar to set the sensor trigger
        scale1 = tk.Scale(self, from_=0, to=100, length=200, tickinterval=25, orient=tk.HORIZONTAL)
        scale1.set(0)
        scale1.grid(row=6, column=0)

        ''''
        ALL SPINBOXES FOR CONTROLUNIT
        '''

        # Spinbox to set the minimal unrolling position of the sunshade
        spinbox1 = tk.Spinbox(self, from_=0, to=100)
        spinbox1.grid(row=2, column=0, sticky=tk.W)

        # Spinbox to set the maximum unrolling position of the sunshade
        spinbox2 = tk.Spinbox(self, from_=0, to=100)
        spinbox2.grid(row=4, column=0, sticky=tk.W)

        # Spinbox to set the custom unrolling position of the sunshade
        spinbox3 = tk.Spinbox(self, from_=0, to=100)
        spinbox3.grid(row=8, column=0, sticky=tk.W)

        ''''
        ALL BUTTONS FOR CONTROLUNIT
        '''

        # The Back button used to go back to the mainpage/frontpage
        but1 = ttk.Button(self, text="Terug", width=10,
                          command=lambda: controller.show_frame("Mainpage"))
        but1.grid(row=9, column=0, sticky=tk.W)

        # A apply button to apply the value that is set for
        # custom unrolling position of the sunshade
        but2 = ttk.Button(self, text="apply", width=10)
        but2.grid(row=8, column=0, sticky=tk.E)

        # Edit settings button
        but3 = ttk.Button(self, text="edit")
        but3.grid(row=0, column=0, sticky=tk.NE)