import tkinter as tk
from tkinter import ttk

from controlunit import ControlUnit, get_COM_ports
from Project import ControlUnitGUI
import matplotlib.animation as animation

''''
The class Mainpage is the front page of the application
It's a frame that shows which controlunit(s) are connected
'''

class Mainpage(tk.Frame):

    control_units = []

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        names = ["Besturingseenheid 1", "Besturingseenheid 2", "asdasd 3"]
      #  for i in names:
     #       Mainpage.newc(self, i, names.index(i)) # passes the string and index position in the list of names

        # Mainpage.newc(self, name, 0)
        # Mainpage.newc(self, name, 1)
        # Mainpage.newc(self, 2)
        # Mainpage.newc(self, 3)
        # Mainpage.newc(self, 4)

        ports = get_COM_ports()




        for port in ports:
            self.control_units.append(ControlUnit(port.device))

        for index, control_unit in enumerate(self.control_units):
            control_unit.request_connection()
            if(control_unit.connected):
                frame = ControlUnitFrame(self, control_unit, index)
                controlunitframe = ControlUnitGUI.ControlUnit(parent=parent, controller=controller, control_unit=control_unit)
                controlunitframe.grid(row=0, column=0, sticky="nsew")
                controller.frames[control_unit.request_device_name()] = controlunitframe

        ''''
        ALL LABELS FOR MAINPAGE
        '''
        # def scan(self):
        #     ports = ge
        #     for p in ports:
        #         print(p)
        #
        # scanbutton = ttk.Button(self, text="Scan for devices")
        # scanbutton.bind("<Button-1>", scan)
        # scanbutton.grid(row=0)


class ControlUnitFrame:
    def __init__(self, parent, control_unit, col):
        self.parent = parent
        self.control_unit = control_unit
        self.device_name = control_unit.request_device_name()
        self.name_label = tk.Label()
        self.newc(col)

    def newc(self, col): # name is a string and col is the index position at which to place the control unit
        marginframe = tk.Frame(self.parent, padx=10, pady=10, width=300)  # generates a frame within the frame with padding set to 10
        marginframe.grid(row=1, column=col)
        borderframe = tk.Frame(marginframe, highlightbackground="grey", highlightthickness=1, padx=10, pady=10)
        # generates a tk.frame within another frame, to get the padding/margin right. padx/pady set to 10
        borderframe.grid(row=1)

        # print(borderframe.grid_info())

        rolloutstatus = "Uiterold: " # shows rollout status
        sensorvalue = "Sensorwaarde: " # shows sensor value
        # a line of text
        self.name_label = tk.Label(borderframe, text=self.device_name, width=20)
        self.name_label.grid(row=1, column=0)

        # a row of white space
        emptylabel = tk.Label(borderframe)
        emptylabel.grid(row=2, column=0)

        # a line of text
        rolloutlabel = tk.Label(borderframe, text=rolloutstatus)
        rolloutlabel.grid(row=3, column=0)

        # a line of text
        sensorvaluelabel = tk.Label(borderframe, text=sensorvalue)
        sensorvaluelabel.grid(row=4, column=0)

        ''''
        ALL BUTTONS FOR MAINPAGE
        '''
        # Button to roll up the sunshade
        rollupbut = ttk.Button(borderframe, text="Oprollen", width=10)
        rollupbut.grid(row=5, column=0)

        # Button to roll out the sunshade
        rolloutbut = ttk.Button(borderframe, text="Uitrollen", width=10)
        rolloutbut.grid(row=6, column=0)

        # Button to go to detailed information about a particulair Controlunit
        overviewbut = ttk.Button(borderframe, text="Overzicht", width=10,
                          command=lambda: self.parent.controller.show_frame(self.device_name))
        overviewbut.grid(row=7, column=0)